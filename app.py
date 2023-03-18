from flask import Flask
import json
from bson import json_util
from services.days import Days

app = Flask(__name__)

@app.route('/api/days/bydate/<date>', methods=["GET"])
def get_day_bydate(date):
  day_to_send=Days.get_day_by_date(date)
  return json.loads(json_util.dumps(day_to_send))


@app.route('/api/days/byid/<id>',methods=["GET"])
def get_day_by_id(id):
  day_to_send= Days.get_day_by_id(id)
  return  json.loads(json_util.dumps(day_to_send))


app.run( debug=True,host='0.0.0.0')

if __name__ == '__main__':
    app.run()