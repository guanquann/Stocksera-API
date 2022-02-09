import requests
import pandas as pd
from datetime import datetime

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Stock:
    def sec_fillings(self, ticker, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        data = requests.get(f"{BASE_URL}/sec_fillings/{ticker}/?date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data)

    def news_sentiment(self, ticker):
        data = requests.get(f"{BASE_URL}/news_sentiment/{ticker}").json()
        return pd.DataFrame(data)

    def insider_trading(self, ticker="", limit=500, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        if not ticker:
            data = requests.get(f"{BASE_URL}/latest_insider/?limit={str(limit)}").json()
        else:
            data = requests.get(f"{BASE_URL}/insider_trading/{ticker}/?date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data)

    def latest_insider_trading_summary(self):
        data = requests.get(f"{BASE_URL}/latest_insider_summary").json()
        return pd.DataFrame(data)

    def short_volume(self, ticker="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        if not ticker:
            data = requests.get(f"{BASE_URL}/top_short_volume").json()
        else:
            data = requests.get(f"{BASE_URL}/short_volume/{ticker}/?date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data)

    def ftd(self, ticker="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        if not ticker:
            data = requests.get(f"{BASE_URL}/top_failure_to_deliver").json()
        else:
            data = requests.get(f"{BASE_URL}/failure_to_deliver/{ticker}/?date_from={date_from}&date_to={date_to}").json()
        return pd.DataFrame(data)

    def earnings_calendar(self, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        data = requests.get(f"{BASE_URL}/earnings_calendar/?date_from={date_from}&date_to={date_to}").json()
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
