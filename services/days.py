import sys
sys.path.append('../modules')
import datetime
import pymongo
from modules.stockSchema import ValidateData 

# # ? connect to mongo db atlas server
client = pymongo.MongoClient(
    "mongodb+srv://davidkvarts:1136896@stocksmovers.ij4fb36.mongodb.net/test")
stock_movers = client["StockMovers"]
days = stock_movers["Days"]


class Days:
    def insert_new_day(day):
        try:
            day["datetime"] = str(datetime.datetime.now())
            print(day)
            ValidateData.validateDay(day)
            result=days.insert_one(day)
            return result.inserted_id
        except Exception as e:
            print(e)


