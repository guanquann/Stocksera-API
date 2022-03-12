import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Social:
    def subreddit(self, ticker="GME", days=30):
        url = f"{BASE_URL}/subreddit_count/{ticker}/"
        if days:
            url += f"?days={str(days)}"
        data = requests.get(url).json()
        return pd.DataFrame(data)

    def wsb_mentions(self, ticker="", days=1):
        url = f"{BASE_URL}/reddit/wsb/"
        if ticker:
            url += f"{ticker}/"
        if days:
            url += f"?days={str(days)}"
        data = requests.get(url).json()
        return pd.DataFrame(data)

    def wsb_options(self, days=1):
        url = f"{BASE_URL}/wsb_options/"
        if days:
            url += f"?days={str(days)}"
        data = requests.get(url).json()
        return pd.DataFrame(data)

    def stocktwits(self, ticker):
        data = requests.get(f"{BASE_URL}/stocktwits/{ticker}").json()
        return pd.DataFrame(data)
