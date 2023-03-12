from flask import Flask
import requests


from services.gainers import GainersStocks
from services.active import ActiveStocks
from services.days import Days
from services.lossers import LosersStocks

app = Flask(__name__)

@app.route('/api/days', methods=["GET"])
def get_all_days():
    return 'all days data'

def get_todays_stocks(day):
    try:
        actives_ids= ActiveStocks.insert_new_stocks(day["actives"])
        gainers_ids=GainersStocks.insert_new_stocks(day["gainers"])
        losers_ids=LosersStocks.insert_new_stocks(day["losers"])
        day_to_add= {
        "actives":actives_ids,
        "gainers":gainers_ids,
        "losers":losers_ids
        }
        result = Days.insert_new_day(day_to_add)
        return str(result.inserted_id)
    except Exception as e:
        raise e
   

    
data={
  "gainers": [
    {
      "netChange": 8.25,
      "volume": 9137,
      "ticker": "MAXN",
      "performanceID": "0P0001KJM8",
      "name": "Maxeon Solar Technologies Ltd",
      "exchange": "XNAS",
      "percentNetChange": 44,
      "lastPrice": 27
    },
    {
      "netChange": 2.23,
      "volume": 100131,
      "ticker": "DSEY",
      "performanceID": "0P0001LXZZ",
      "name": "Diversey Holdings Ltd",
      "exchange": "XNAS",
      "percentNetChange": 37.479,
      "lastPrice": 8.18
    },
    {
      "netChange": 3.56,
      "volume": 3731,
      "ticker": "VERX",
      "performanceID": "0P0001KE2E",
      "name": "Vertex",
      "exchange": "XNAS",
      "percentNetChange": 23.7175,
      "lastPrice": 18.57
    },
    {
      "netChange": 4.27,
      "volume": 77,
      "ticker": "TMCI",
      "performanceID": "0P0001M62W",
      "name": "Treace Medical Concepts",
      "exchange": "XNAS",
      "percentNetChange": 21.1073,
      "lastPrice": 24.5
    },
    {
      "netChange": 1.14,
      "volume": 79,
      "ticker": "MCG",
      "performanceID": "0P0001MV9H",
      "name": "Membership Collective Group",
      "exchange": "XNYS",
      "percentNetChange": 18.2109,
      "lastPrice": 7.4
    },
    {
      "netChange": 0.86,
      "volume": 1326,
      "ticker": "LFST",
      "performanceID": "0P0001MLNW",
      "name": "LifeStance Health Group",
      "exchange": "XNAS",
      "percentNetChange": 18.1435,
      "lastPrice": 5.6
    },
    {
      "netChange": 0.3,
      "volume": 5045,
      "ticker": "GOL",
      "performanceID": "0P000002GM",
      "name": "Gol Linhas Aereas Inteligentes SA",
      "exchange": "XNYS",
      "percentNetChange": 11.4504,
      "lastPrice": 2.92
    },
    {
      "netChange": 3.7,
      "volume": 865,
      "ticker": "NVEI",
      "performanceID": "0P0001L02S",
      "name": "Nuvei Corp",
      "exchange": "XNAS",
      "percentNetChange": 11.3115,
      "lastPrice": 36.41
    },
    {
      "netChange": 0.89,
      "volume": 2392,
      "ticker": "YEXT",
      "performanceID": "0P0001A2H5",
      "name": "Yext",
      "exchange": "XNYS",
      "percentNetChange": 10.4829,
      "lastPrice": 9.38
    },
    {
      "netChange": 0.9,
      "volume": 19074,
      "ticker": "AUPH",
      "performanceID": "0P0000BLCT",
      "name": "Aurinia Pharmaceuticals",
      "exchange": "XNAS",
      "percentNetChange": 9.9558,
      "lastPrice": 9.94
    }
  ],
  "actives": [
    {
      "netChange": -5.71,
      "volume": 2846423,
      "ticker": "TSLA",
      "performanceID": "0P0000OQN8",
      "name": "Tesla",
      "exchange": "XNAS",
      "percentNetChange": -3.0419,
      "lastPrice": 182
    },
    {
      "netChange": 0.49,
      "volume": 178021,
      "ticker": "RIVN",
      "performanceID": "0P0001NP95",
      "name": "Rivian Automotive",
      "exchange": "XNAS",
      "percentNetChange": 3.347,
      "lastPrice": 15.13
    },
    {
      "netChange": 2.23,
      "volume": 100131,
      "ticker": "DSEY",
      "performanceID": "0P0001LXZZ",
      "name": "Diversey Holdings Ltd",
      "exchange": "XNAS",
      "percentNetChange": 37.479,
      "lastPrice": 8.18
    },
    {
      "netChange": 3.26,
      "volume": 156885,
      "ticker": "AMD",
      "performanceID": "0P0000006A",
      "name": "Advanced Micro Devices",
      "exchange": "XNAS",
      "percentNetChange": 3.9703,
      "lastPrice": 85.37
    },
    {
      "netChange": 8.93,
      "volume": 415273,
      "ticker": "NVDA",
      "performanceID": "0P000003RE",
      "name": "NVIDIA Corp",
      "exchange": "XNAS",
      "percentNetChange": 3.8346,
      "lastPrice": 241.81
    },
    {
      "netChange": 1.27,
      "volume": 198800,
      "ticker": "AAPL",
      "performanceID": "0P000000GY",
      "name": "Apple",
      "exchange": "XNAS",
      "percentNetChange": 0.8377,
      "lastPrice": 152.87
    },
    {
      "netChange": 0.15,
      "volume": 94984,
      "ticker": "F",
      "performanceID": "0P0000029A",
      "name": "Ford Motor Company",
      "exchange": "XNYS",
      "percentNetChange": 1.1691,
      "lastPrice": 12.98
    },
    {
      "netChange": 0.37,
      "volume": 152877,
      "ticker": "AMZN",
      "performanceID": "0P000000B7",
      "name": "Amazon.com",
      "exchange": "XNAS",
      "percentNetChange": 0.3955,
      "lastPrice": 93.92
    },
    {
      "netChange": -0.44,
      "volume": 77526,
      "ticker": "BAC",
      "performanceID": "0P000000PA",
      "name": "Bank of America Corp",
      "exchange": "XNYS",
      "percentNetChange": -1.3333,
      "lastPrice": 32.56
    },
    {
      "netChange": 0.21,
      "volume": 261179,
      "ticker": "NIO",
      "performanceID": "0P0001EEPZ",
      "name": "NIO",
      "exchange": "XNYS",
      "percentNetChange": 2.3411,
      "lastPrice": 9.18
    }
  ],
  "losers": [
    {
      "netChange": -11.49,
      "volume": 2676,
      "ticker": "UNFI",
      "performanceID": "0P000005N9",
      "name": "United Natural Foods",
      "exchange": "XNYS",
      "percentNetChange": -28.0518,
      "lastPrice": 29.47
    },
    {
      "netChange": -2.96,
      "volume": 4461,
      "ticker": "HCM",
      "performanceID": "0P00017LBQ",
      "name": "HUTCHMED (China) Limited",
      "exchange": "XNAS",
      "percentNetChange": -17.9068,
      "lastPrice": 13.57
    },
    {
      "netChange": -2.15,
      "volume": 2920,
      "ticker": "BBIO",
      "performanceID": "0P0001HT9M",
      "name": "BridgeBio Pharma",
      "exchange": "XNAS",
      "percentNetChange": -11.5903,
      "lastPrice": 16.4
    },
    {
      "netChange": -3.45,
      "volume": 1570971,
      "ticker": "VRDN",
      "performanceID": "0P0001359S",
      "name": "Viridian Therapeutics",
      "exchange": "XNAS",
      "percentNetChange": -10.48,
      "lastPrice": 29.47
    },
    {
      "netChange": -3.12,
      "volume": 1,
      "ticker": "HNI",
      "performanceID": "0P000002KC",
      "name": "HNI Corp",
      "exchange": "XNYS",
      "percentNetChange": -10.4208,
      "lastPrice": 26.82
    },
    {
      "netChange": -0.81,
      "volume": 2,
      "ticker": "SCLX",
      "performanceID": "0P0001Q1GZ",
      "name": "Scilex Holding Company",
      "exchange": "XNAS",
      "percentNetChange": -9.1422,
      "lastPrice": 8.05
    },
    {
      "netChange": -2.28,
      "volume": 222,
      "ticker": "SHLS",
      "performanceID": "0P0001LJDR",
      "name": "Shoals Technologies Group",
      "exchange": "XNAS",
      "percentNetChange": -8.5876,
      "lastPrice": 24.27
    },
    {
      "netChange": -1.01,
      "volume": 184664,
      "ticker": "TDCX",
      "performanceID": "0P0001NFYF",
      "name": "TDCX",
      "exchange": "XNYS",
      "percentNetChange": -7.7158,
      "lastPrice": 12.08
    },
    {
      "netChange": -3.21,
      "volume": 163055,
      "ticker": "VVX",
      "performanceID": "0P000148FH",
      "name": "V2X",
      "exchange": "XNYS",
      "percentNetChange": -7.1732,
      "lastPrice": 41.54
    },
    {
      "netChange": -0.42,
      "volume": 12,
      "ticker": "GETY",
      "performanceID": "0P0001PFWZ",
      "name": "Getty Images Holdings",
      "exchange": "XNYS",
      "percentNetChange": -7.1672,
      "lastPrice": 5.44
    }
  ]
}
print(get_todays_stocks(data))

app.run(debug=True, host='0.0.0.0')
