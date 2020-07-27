#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This code scraps mohfw.gov.in for COVID-19 Data

"""
import requests
import json
import logging
import threading

from flask import Flask
from flask import jsonify

from bs4 import BeautifulSoup
from datetime import datetime

# Removed Foreign National Column
headers = {
    0: "id",
    1: "place",
    2: "active",
    3: "cured",
    4: "deaths",
    5: "total_confirmed"
}

# Initialisations
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)
app = Flask(__name__)

# config
FETCH_INTERVAL = 1800

# global response variable, to be overwritten later
last_extracted_content = {"data": "fetching.. please try again in a minute"}

# scrapes table from the given url
def get_table_from_web():
    url = "http://mohfw.gov.in"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', class_='data-table')
    table = div.find('table', class_='table')
    return table

# When provided with rows of a table, returns state_data, after cleaning
# Assumed that state data will be for first 35 rows in body of table
def get_state_wise_data(rows):
    rows = rows[:36]
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

# When provided with rows of a table, returns total_data, assuming that 36th row is total_data
def get_total_data(rows):
    total = rows[36].find_all("strong")
    total_data = {}
    for index in headers:
        if index != 0 and index != 1:
            total_data[headers[index]] = total[index-1].text
    return total_data

# get_data combines all the information given extracted table content
def get_data(content, time, indent=None):
    rows = content.find_all("tr")
    
    state_data = get_state_wise_data(rows) # consider all rows except the last 6
    
    total_data = get_total_data(rows)
    
    response = {
        "data": {
            "state_data": state_data,
            "total_data": total_data,
            "last_updated": str(time)
        }
    }
    
    return response

# parent function that calls the scraping function and get_data function
def data_extract():
    table = get_table_from_web()
    logging.info("Table fetched. \n Fetching state wise data from table...\n")
    
    state_wise_data = get_data(table, datetime.now())
    logging.info("Fetched state wise data.\n")
    
    global last_extracted_content
    last_extracted_content = state_wise_data

@app.route('/', methods=['GET'])
def home():
    return '''
    <h1>COVID 19 India Data</h1>
    <h3> API Version: v1 </h3>
    <h3>Source: <a href="https://mohfw.gov.in">Ministry of Health and Family Welfare, India</a></h3>
    <h3><a href="https://covid-india-api.herokuapp.com/v1/api">Click here</a> to get data as JSON<h3>'''


@app.route('/v1/api', methods=['GET'])
def api():
    global last_extracted_content
    logging.info("Request received, response: %s", last_extracted_content)
    return jsonify(last_extracted_content)

def start_thread():
    threading.Timer(FETCH_INTERVAL, data_extract, ()).start()

if __name__ == "__main__":
    logging.info("****** COVID-INDIA-API *******")
    app.run(debug=True)