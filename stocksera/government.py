import requests
import json
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api/"


class Government:
    def senate(self):
        r = requests.get(f"{BASE_URL}/senate_trades")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def house(self):
        r = requests.get(f"{BASE_URL}/house_trades")
        j = json.loads(r.content)
        return pd.DataFrame(j)