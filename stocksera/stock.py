import requests
import json
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api/"


class Stock:
    def sec_fillings(self, ticker="AAPL"):
        r = requests.get(f"{BASE_URL}/sec_fillings/{ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def news_sentiment(self, ticker="AAPL"):
        r = requests.get(f"{BASE_URL}/news_sentiment/{ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def insider_trading(self, ticker=""):
        if not ticker:
            r = requests.get(f"{BASE_URL}/latest_insider")
        else:
            r = requests.get(f"{BASE_URL}/insider_trading/{ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def latest_insider_trading_summary(self):
        r = requests.get(f"{BASE_URL}/latest_insider_summary")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def short_volume(self, ticker=""):
        if not ticker:
            r = requests.get(f"{BASE_URL}/top_short_volume")
        else:
            r = requests.get(f"{BASE_URL}/short_volume/{ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def ftd(self, ticker=""):
        if not ticker:
            r = requests.get(f"{BASE_URL}/top_failure_to_deliver")
        else:
            r = requests.get(f"{BASE_URL}/failure_to_deliver/{ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def earnings_calendar(self):
        r = requests.get(f"{BASE_URL}/earnings_calendar")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def short_interest(self):
        r = requests.get(f"{BASE_URL}/short_interest")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def low_float(self):
        r = requests.get(f"{BASE_URL}/low_float")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def stocktwits(self, ticker="TSLA"):
        r = requests.get(f"{BASE_URL}/stocktwits/{ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def ipo_calendar(self):
        r = requests.get(f"{BASE_URL}/ipo_calendar")
        j = json.loads(r.content)
        return pd.DataFrame(j)
