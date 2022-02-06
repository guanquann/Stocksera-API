import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Stock:
    def sec_fillings(self, ticker):
        data = requests.get(f"{BASE_URL}/sec_fillings/{ticker}").json()
        return pd.DataFrame(data)

    def news_sentiment(self, ticker):
        data = requests.get(f"{BASE_URL}/news_sentiment/{ticker}").json()
        return pd.DataFrame(data)

    def insider_trading(self, ticker="", limit=500):
        if not ticker:
            data = requests.get(f"{BASE_URL}/latest_insider/?limit={str(limit)}").json()
        else:
            data = requests.get(f"{BASE_URL}/insider_trading/{ticker}").json()
        return pd.DataFrame(data)

    def latest_insider_trading_summary(self):
        data = requests.get(f"{BASE_URL}/latest_insider_summary").json()
        return pd.DataFrame(data)

    def short_volume(self, ticker=""):
        if not ticker:
            data = requests.get(f"{BASE_URL}/top_short_volume").json()
        else:
            data = requests.get(f"{BASE_URL}/short_volume/{ticker}").json()
        return pd.DataFrame(data)

    def ftd(self, ticker=""):
        if not ticker:
            data = requests.get(f"{BASE_URL}/top_failure_to_deliver").json()
        else:
            data = requests.get(f"{BASE_URL}/failure_to_deliver/{ticker}").json()
        return pd.DataFrame(data)

    def earnings_calendar(self):
        data = requests.get(f"{BASE_URL}/earnings_calendar").json()
        return pd.DataFrame(data)

    def short_interest(self):
        data = requests.get(f"{BASE_URL}/short_interest").json()
        return pd.DataFrame(data)

    def low_float(self):
        data = requests.get(f"{BASE_URL}/low_float").json()
        return pd.DataFrame(data)

    def ipo_calendar(self):
        data = requests.get(f"{BASE_URL}/ipo_calendar").json()
        return pd.DataFrame(data)
