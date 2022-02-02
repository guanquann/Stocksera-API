import requests
import json
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api/"


class Economy:
    def reverse_repo(self):
        r = requests.get(f"{BASE_URL}/reverse_repo")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def daily_treasury(self):
        r = requests.get(f"{BASE_URL}/daily_treasury")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def inflation(self):
        r = requests.get(f"{BASE_URL}/inflation")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def retail_sales(self):
        r = requests.get(f"{BASE_URL}/retail_sales")
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def jobless_claims(self):
        r = requests.get(f"{BASE_URL}/initial_jobless_claims")
        j = json.loads(r.content)
        return pd.DataFrame(j)
