import schedule
import time
import datetime
import requests
from services.gainers import GainersStocks
from services.active import ActiveStocks
from services.lossers import LosersStocks
from services.investingScript import get_today_stats
from services.days import Days

def get_todays_stocks(day):
    try:
        actives_ids = ActiveStocks.insert_new_stocks(day["actives"])
        gainers_ids = GainersStocks.insert_new_stocks(day["gainers"])
        losers_ids = LosersStocks.insert_new_stocks(day["losers"])
        day_to_add = {
        "actives" : [str(a) for a in actives_ids],
        "gainers" : [str(a) for a in gainers_ids],
        "losers" : [str(a) for a in losers_ids],
        "indexes" :  get_today_stats()
        }
        # print(1)
        result = Days.insert_new_day(day_to_add)
        print(result)
        return result
    except Exception as e:
        return "error!"

def get_day():

    url = "https://ms-finance.p.rapidapi.com/market/v2/get-movers"

    headers = {
        "X-RapidAPI-Key": "050b19bf01msha30f9f77b131d93p1d3c41jsn74aa161c717b",
        "X-RapidAPI-Host": "ms-finance.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    print(response)
    print(get_todays_stocks(response.json()))



schedule.every().monday.at("23:00").do(get_day)
schedule.every().tuesday.at("23:00").do(get_day)
schedule.every().wednesday.at("23:00").do(get_day)
schedule.every().thursday.at("23:00").do(get_day)
schedule.every().friday.at("23:00").do(get_day)

while True:
    now = datetime.datetime.now()
    if now.weekday() < 5:
        schedule.run_pending()
    time.sleep(1)


