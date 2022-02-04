import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Government:
    def senate(self, name="", ticker=""):
        r = requests.get(f"{BASE_URL}/government/senate/?name={name}&ticker={ticker}")
        content = r.json()
        if ticker:
            content = content[ticker]
        elif name:
            content = content[name]
        return pd.DataFrame(content)

    def house(self, name="", ticker="", state=""):
        r = requests.get(f"{BASE_URL}/government/house/?name={name}&ticker={ticker}&state={state}")
        content = r.json()
        if ticker:
            content = content[ticker]
        elif name:
            content = content[name]
        elif state:
            content = content[state]
        return pd.DataFrame(content)
