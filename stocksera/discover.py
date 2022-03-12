import requests
import pandas as pd
from datetime import datetime

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Discover:
    def jim_cramer(self, ticker="", segment="", call=""):
        r = requests.get(f"{BASE_URL}/jim_cramer/{ticker}/?segment={segment}&call={call}")
        return pd.DataFrame(r.json())

    def short_interest(self):
        data = requests.get(f"{BASE_URL}/short_interest").json()
        return pd.DataFrame(data)

    def low_float(self):
        data = requests.get(f"{BASE_URL}/low_float").json()
        return pd.DataFrame(data)

    def earnings_calendar(self, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        data = requests.get(f"{BASE_URL}/earnings_calendar/?date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data)

    def ipo_calendar(self):
        data = requests.get(f"{BASE_URL}/ipo_calendar").json()
        return pd.DataFrame(data)
