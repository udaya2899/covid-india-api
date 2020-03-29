#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This code scraps mohfw.gov.in for COVID-19 Data

"""
import requests
from bs4 import BeautifulSoup
import json
import dateutil.parser as dparser
from flask import Flask


app = Flask(__name__)
#app.config["DEBUG"] = True

headers = {
    0: "id",
    1: "place",
    2: "confirmed_indian",
    3: "confirmed_foreign",
    4: "cured",
    5: "deaths"
}


def get_table_from_web():
    url = "https://mohfw.gov.in"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', id='cases')
    time = div.find('strong').text
    table = div.find('table', class_='table')
    return table, time


def html_to_json(content, time, indent=None):
    rows = content.find_all("tr")
    data = []
    for row in rows:
        cells = row.find_all("td")

        if len(cells) != 0 and len(cells) == len(headers):
            items = {}
            for index in headers:
                items[headers[index]] = cells[index].text.replace(
                    '\n', '').replace('#', '')

            data.append(items)
            body = {}
            body["state_data"] = data

    for row in rows[-1:]:
        cells = row.find_all("td")
        total_items = {}
        for index in headers:
            if index != 0 and index != 1:
                total_items[headers[index]] = cells[index -
                                                    1].text.replace('\n', '').replace('#', '')
    body["total_data"] = total_items
    body["last_updated"] = str(time)
    response = {}
    response["data"] = body
    return json.dumps(response, indent=indent)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>COVID 19 India Data</h1>
    <h3>Source: <a href="https://mohfw.gov.in">Ministry of Health and Family Welfare, India</a></h3>
    <h3><a href="https://covid-india-api.herokuapp.com/api">Click here</a> to get data as JSON<h3>'''


@app.route('/api', methods=['GET'])
def get_data():
    table, time = get_table_from_web()
    last_updated = dparser.parse(time, fuzzy=True)
    state_wise_data = html_to_json(table, last_updated)
    return state_wise_data


if __name__ == "__main__":
    app.run()
