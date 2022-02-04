import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class ETF:
    def market_summary(self, market_type="snp500"):
        r = requests.get(f"{BASE_URL}/market_summary/?type={market_type}")
        return pd.DataFrame(list(r.json().values())[0])

    def jim_cramer(self):
        r = requests.get(f"{BASE_URL}/jim_cramer")
        return pd.DataFrame(r.json())
