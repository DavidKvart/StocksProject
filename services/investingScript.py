import requests
from bs4 import BeautifulSoup

def get_today_stats():

    result = requests.get('https://www.morningstar.com/')



    doc = BeautifulSoup(result.text, "html.parser")
    #print(doc.prettify())
    table = doc.find("tbody", class_="mdc-table-body mds-data-table__body")
    rows = table.find_all("tr")

    end_of_day_stats = {}

    for index in rows:
        price_change = index.find_all("div", class_="mdc-table-performance-cell__inner")[-1].span.string
        price_change = price_change.strip()[0:-1]
        price_change = float(price_change.replace("−", "-"))

        name = index.a.string.split("\t")[2].split("\n")[0]
        end_of_day_stats[name]=price_change

    return end_of_day_stats

