from jsonschema import validate

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
     "required": ["netChange", "volume",  "ticker","name","lastPrice","precentNetChange"],
}
day_schema={
    "type" : "object",
    "properties" : {
        "datetime" : {"type" : "number"},
        "gainers" : {"type": "array", "items": {"type": "string"}},
        "loosers" : {"type": "array", "items": {"type": "string"}},
        "actives" : {"type": "array", "items": {"type": "string"}},
    },
      "required": ["datetime", "gainers",  "loosers","actives"],
}

class ValidateData:
    def validateStock(stock):
        return validate(instance=stock,schema=stock_schema)
    def validateDay(day):
        return validate(instance=day, schema=day_schema)
