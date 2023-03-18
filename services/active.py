import pymongo
import sys
sys.path.append('../modules')
from modules.stockSchema import ValidateData

# ? connect to mongo db atlas server
client = pymongo.MongoClient(
    "mongodb+srv://davidkvarts:1136896@stocksmovers.ij4fb36.mongodb.net/test")
stock_movers = client["StockMovers"]
active_stock = stock_movers["ActiveStocks"]


class ActiveStocks:
    def insert_new_stocks(stocks):
       
        try:
            for stock in stocks:
                ValidateData.validateStock(stock)
            result = active_stock.insert_many(stocks)

            return result.inserted_ids

        except Exception as e:
            return e



