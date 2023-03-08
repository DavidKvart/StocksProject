import pymongo
import sys
sys.path.append('C:/Users/David kvart/pythonProjects/practiceProject/modules')
from stockSchema import ValidateData

#? connect to mongo db atlas server
client = pymongo.MongoClient("mongodb+srv://davidkvarts:1136896@stocksmovers.ij4fb36.mongodb.net/test")
stock_movers = client["StockMovers"]
days=stock_movers["Days"]


class ActiveStocks:
    def insert_new_day(day):
        try:
            for stock in stocks:
                ValidateData.validateStock(stock)  
            result=active_stock.insert_many(stocks)
            return str(result.inserted_ids)
        
        except Exception as e:
            return e
        
   
        
        
        