from flask import Flask
import requests
#! add the modules and server classes

app = Flask(__name__)

@app.route('/api/days', methods=["GET"])
def get_all_days():
    return 'all days data'

app.run(debug=True, host='0.0.0.0')
