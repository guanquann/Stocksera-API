import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Government:
    def senate(self, name="", ticker=""):
        data = requests.get(f"{BASE_URL}/government/senate/?name={name}&ticker={ticker}").json()
        return pd.DataFrame(data["senate"])

    def house(self, name="", ticker="", state=""):
        data = requests.get(f"{BASE_URL}/government/house/?name={name}&ticker={ticker}&state={state}").json()
        return pd.DataFrame(data["house"])
