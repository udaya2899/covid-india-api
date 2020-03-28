
# Covid India API
> REST API to track Coronavirus cases in India on state level

> COVID 19 India States Data API

![enter image description here](https://img.shields.io/github/issues/udaya2899/covid-india-api) ![enter image description here](https://img.shields.io/github/forks/udaya2899/covid-india-api) ![enter image description here](https://img.shields.io/github/stars/udaya2899/covid-india-api) ![enter image description here](https://img.shields.io/github/license/udaya2899/covid-india-api)

Coronavirus is shaking the world :earth_africa:. At such crucial times, the purity of data is to be maintained. Govt. of India hasn't released an official API yet. This API scraps data from Official Website of [Ministry of Health and Family Welfare](https://mohfw.gov.in) :heavy_check_mark: and exposes them as a **REST API** at [https://covid-india-api.herokuapp.com/api](https://covid-india-api.herokuapp.com/api)


# Usage :computer:
### REST API Sample Usage
cURL Command:

    curl --request GET "https://covid-india-api.herokuapp.com/api"
	
### To run the server locally on your machine:

    
    git clone https://github.com/udaya2899/covid-india-api.git
    cd covid-india-api
    pip install -r requirements.txt
    python app.py

## Implementation :construction_worker:

 - :snake: **Python 3** 
 - :sake: **Flask** - REST GET Implementation
 - :stew: **BeautifulSoup** - Web Scraping
 - :arrow_right: **JSON** - Data Serialization
 - :six_pointed_star: **Heroku** - Deployment


## Requirements :zap:
Refer to `requirements.txt` for full list of requirements

    beautifulsoup4==4.8.2
    Flask==1.1.1
    python-dateutil==2.8.1
    requests==2.23.0
## Data Source - Sample Table :white_check_mark:
Sample data from Ministry of Health and Family Welfare, Govt. of India [(link)](https://mohfw.gov.in)

![MOHFW Sample Data Table](https://i.imgur.com/W4wNB1w.png)

## API - Sample JSON :rocket:

Sample API Response obtained from [https://covid-india-api.herokuapp.com/api](https://covid-india-api.herokuapp.com/api)

     {
      "data": {
        "state_data": [
          {
            "id": "1",
            "place": "Andhra Pradesh",
            "confirmed_indian": "14",
            "confirmed_foreign": "0",
            "cured": "1",
            "deaths": "0"
          },
          {
            "id": "2",
            "place": "Andaman and Nicobar Islands",
            "confirmed_indian": "6",
            "confirmed_foreign": "0",
            "cured": "0",
            "deaths": "0"
          },
          .
          .
          .
	      {
		    "id": "27", 
		    "place": "West Bengal", 
		    "confirmed_indian": "15", 
		    "confirmed_foreign": "0", 
		    "cured": "0", 
		    "deaths": "1"
		  }
        ]
        "total_data": {
	        "confirmed_indian": "862", 
	        "confirmed_foreign": "47 ", 
	        "cured": "80", 
	        "deaths": "19"
	        }, 
	     "last_updated": "2020-03-28 17:45:00"
	     }
	  }
    }

## Contribution :handshake:
Pull requests are welcomed to make changes. To make drastic changes, open an issue to discuss.

## Contact  :mailbox:
Mail me at udayaprakash2899@gmail.com for further queries 

