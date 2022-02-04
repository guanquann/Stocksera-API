import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Economy:
    def reverse_repo(self):
        r = requests.get(f"{BASE_URL}/reverse_repo")
        return pd.DataFrame(r.json())

    def daily_treasury(self):
        r = requests.get(f"{BASE_URL}/daily_treasury")
        return pd.DataFrame(r.json())

    def inflation(self):
        r = requests.get(f"{BASE_URL}/inflation")
        return pd.DataFrame(r.json())

    def retail_sales(self):
        r = requests.get(f"{BASE_URL}/retail_sales")
        return pd.DataFrame(r.json())

    def jobless_claims(self):
        r = requests.get(f"{BASE_URL}/initial_jobless_claims")
        return pd.DataFrame(r.json())

