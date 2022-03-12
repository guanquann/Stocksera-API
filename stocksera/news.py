import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class News:
    def trading_halts(self):
        data = requests.get(f"{BASE_URL}/trading_halts").json()
        return pd.DataFrame(data)

    def market_news(self):
        data = requests.get(f"{BASE_URL}/market_news").json()
        return pd.DataFrame(data)
