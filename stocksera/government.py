import requests
import json
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api/"


class Government:
    def senate(self, name="", ticker=""):
        r = requests.get(f"{BASE_URL}/senate_trades/?name={name}&ticker={ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def house(self, name="", ticker=""):
        r = requests.get(f"{BASE_URL}/house_trades/?name={name}&ticker={ticker}")
        j = json.loads(r.content)
        return pd.DataFrame(j)
