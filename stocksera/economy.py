import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Economy:
    def reverse_repo(self, days=100):
        url = f"{BASE_URL}/reverse_repo/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        return pd.DataFrame(r.json())

    def daily_treasury(self, days=100):
        url = f"{BASE_URL}/daily_treasury/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        return pd.DataFrame(r.json())

    def inflation(self):
        r = requests.get(f"{BASE_URL}/inflation")
        return pd.DataFrame(r.json())

    def retail_sales(self, days=100):
        url = f"{BASE_URL}/retail_sales/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        return pd.DataFrame(r.json())

    def jobless_claims(self, days=100):
        url = f"{BASE_URL}/initial_jobless_claims/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        return pd.DataFrame(r.json())
