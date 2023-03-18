import sys
sys.path.append('../modules')
from datetime import datetime,timedelta
import re
import pymongo
from modules.stockSchema import ValidateData 
from bson.objectid import ObjectId

# # ? connect to mongo db atlas server
client = pymongo.MongoClient(
    "mongodb+srv://davidkvarts:1136896@stocksmovers.ij4fb36.mongodb.net/test")
stock_movers = client["StockMovers"]
days = stock_movers["Days"]
gainers_stock=stock_movers["GainersStocks"]
lossers_stock=stock_movers["LosserStocks"]
active_stock = stock_movers["ActiveStocks"]

class Days:
    def insert_new_day(day):
        try:
            day["datetime"] = str(datetime.now())
            ValidateData.validateDay(day)
            result=days.insert_one(day)
            return result.inserted_id
        except Exception as e:
            print(e)


    def get_day_by_id(id):
        obj_id=ObjectId(id)
        day_found = days.find_one({"_id" : obj_id})

        if not day_found:
            return None

        day_found["gainers"] = populate_array_of_stocks("GainersStocks", "gainers", day_found )
        day_found["actives"] = populate_array_of_stocks("ActiveStocks","actives",day_found)
        day_found["losers"] =populate_array_of_stocks("LosserStocks","losers",day_found)

        return day_found


    def get_day_by_date(date):
        pattern = re.compile("^"+date)
        day_found = days.find_one({"datetime":{"$regex": pattern} })
        if not day_found:
            return None
        day_found["gainers"] = populate_array_of_stocks("GainersStocks", "gainers", day_found)
        day_found["actives"] = populate_array_of_stocks("ActiveStocks", "actives", day_found)
        day_found["losers"] = populate_array_of_stocks("LosserStocks", "losers", day_found)

        return day_found


# functions
def populate_array_of_stocks(collection_name,array_name,day):
    arr=[]
    collection=stock_movers[collection_name]
    for stockID in day[array_name]:
        stockID = ObjectId(stockID)
        arr.append(collection.find_one({"_id": stockID}))
    return arr

