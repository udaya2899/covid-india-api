# covid-india-api
> REST API to track Coronavirus cases in India on state level
> COVID19 India data

Coronavirus is shaking the world  . At such crucial times, the purity of data is to be maintained. Gov of India hasn't released an official API yet. This API scraps data from Official Website of [Ministry of Health and Family Welfare](https://mohfw.gov.in) and exposes them as a **REST API** at [https://covid-india-api.herokuapp.com/api](https://covid-india-api.herokuapp.com/api)


# Usage

    # To run locally on your machine
    git clone https://github.com/udaya2899/covid-india-api.git
    cd covid-india-api
    pip install -r requirements.txt
    python app.py

## Implementation

 - **Python 3**
 - **Flask** - REST GET Implementation
 - **BeautifulSoup** - Web Scraping
 - **JSON** - Data Serialization
 - **Heroku** - Deployment


## Requirements
Refer to `requirements.txt` for full list of requirements

    beautifulsoup4==4.8.2
    Flask==1.1.1
    python-dateutil==2.8.1
    requests==2.23.0

You can rename the current file by clicking the file name in the navigation bar or by clicking the **Rename** button in the file explorer.

