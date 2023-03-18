from jsonschema import validate
from bson.objectid import ObjectId

stock_schema={
   "type" : "object",
     "properties" : {
        "netChange" : {"type" : "number"},
        "volume" : {"type" : "number"},
        "ticker" : {"type" : "string"},
        "name" : {"type" : "string"},
        "lastPrice" : {"type" : "number"},
        "precentNetChange" : {"type" : "number"},
    },
     "required": ["volume",  "ticker","name","lastPrice"],
}
# region laksjndflknasdfsf
day_schema={
    "type" : "object",
    "properties" : {
        "datetime" : {"type" : "string"},
        "gainers" : {"type": "array", "items": {"type": "string"}},
        "losers" : {"type": "array", "items": {"type": "string"}},
        "actives" : {"type": "array", "items": {"type": "string"}},
        "indexes": {"type" : "object"}
    },
      "required": ["datetime", "gainers",  "losers","actives"],
}
# endregion

class ValidateData:
    def validateStock(stock):
        return validate(instance=stock,schema=stock_schema)
    def validateDay(day):
        return validate(instance=day, schema=day_schema)
