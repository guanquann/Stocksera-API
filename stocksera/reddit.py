import json
import requests
import pandas as pd

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Reddit:
    def subreddit(self, ticker="GME", days=30):
        url = f"{BASE_URL}/subreddit_count/{ticker}/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def wsb_mentions(self, ticker="", days=1):
        url = f"{BASE_URL}/wsb_mentions/"
        if ticker:
            url += f"{ticker}/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        j = json.loads(r.content)
        return pd.DataFrame(j)

    def wsb_options(self, days=1):
        url = f"{BASE_URL}/wsb_options/"
        if days:
            url += f"?days={str(days)}"
        r = requests.get(url)
        j = json.loads(r.content)
        return pd.DataFrame(j)
