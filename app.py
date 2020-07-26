#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This code scraps mohfw.gov.in for COVID-19 Data

"""
import requests
import threading
from bs4 import BeautifulSoup
import json
from flask import Flask
import re
import time
from time import sleep
from datetime import datetime
from flask import request
app = Flask(__name__)

# Removed Foreign National Column
headers = {
    0: "id",
    1: "place",
    2: "active",
    3: "cured",
    4: "deaths",
    5: "total_confirmed"
}
# Added Date Time matching REGEX to give better input to Fuzze Dateutil Parser
last_extracted_content = "Initial fetch... Please try after a minute"

def get_table_from_web():
    url = "http://mohfw.gov.in"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', class_='data-table')
    table = div.find('table', class_='table')
    return table

def get_state_wise_data(rows):
    state_data = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) != 0 and len(cells) == len(headers):
            items = {}
            for index in headers:
                items[headers[index]] = cells[index].text.replace(
                    '\n', '').replace('#', '').replace('*','')
            state_data.append(items)
    return state_data

def get_total_data(rows):
    total = rows[-6].find_all("strong")
    total_data = {}
    for index in headers:
        if index != 0 and index != 1:
            total_data[headers[index]] = total[index-1].text
    return total_data

def get_data(content, time, indent=None):
    rows = content.find_all("tr")
    
    state_data = get_state_wise_data(rows[:len(rows)-6]) # consider all rows except the last 6
    
    total_data = get_total_data(rows)
    
    response = {
        "data": {
            "state_data": state_data,
            "total_data": total_data,
            "last_updated": str(time)
        }
    }
    
    return json.dumps(response, indent=4)


def data_extract():
    print("Thread triggered")
    while(True):
        print("Fetching table from web ...\n")
        table = get_table_from_web()
        print("Table fetched. \n Fetching state wise data from table...\n")
        state_wise_data = get_data(table, datetime.now())
        print("Fetched state wise data.\n")
        global last_extracted_content
        print("Setting last_extracted_content...\n")
        last_extracted_content = state_wise_data
        print("last_extracted_content set, last_extracted_content:", last_extracted_content)
        time.sleep(1800)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>COVID 19 India Data</h1>
    <h3> API Version: v1 </h3>
    <h3>Source: <a href="https://mohfw.gov.in">Ministry of Health and Family Welfare, India</a></h3>
    <h3><a href="https://covid-india-api.herokuapp.com/v1/api">Click here</a> to get data as JSON<h3>
    <h4>Updates every 30 minutes from mohfw.gov.in</h4>'''


@app.route('/v1/api', methods=['GET'])
def api():
    return last_extracted_content


if __name__ == "__main__":
    x = threading.Thread(target=data_extract, args=())
    x.start()
    app.run()
