import pymongo
import json
import sys
sys.path.append('../modules')
from modules.stockSchema import ValidateData

#? connect to mongo db atlas server
client = pymongo.MongoClient("mongodb+srv://davidkvarts:1136896@stocksmovers.ij4fb36.mongodb.net/test")
stock_movers = client["StockMovers"]
gainers_stock=stock_movers["GainersStocks"]


class GainersStocks:
    def insert_new_stocks(stocks):
        try:
            for stock in stocks:
                ValidateData.validateStock(stock)
                
            result=gainers_stock.insert_many(stocks)
            return result.inserted_ids
        
        except Exception as e:
            return e
        

        
        
