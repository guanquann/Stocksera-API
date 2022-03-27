import requests
from datetime import datetime
from stocksera.exceptions import StockseraRequestException

BASE_URL = "https://stocksera.pythonanywhere.com/api"


class Client:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {'accept': 'application/json', 'Authorization': "Token " + self.api_key}

    def _get(self, url):
        r = requests.get(url, headers=self.headers)
        if r.json() == {'Error': 'Invalid API Key / Authorization Headers is empty'}:
            raise StockseraRequestException
        return r.json()

    def jim_cramer(self, ticker="", segment="", call=""):
        url = f"{BASE_URL}/jim_cramer/{ticker}/?segment={segment}&call={call}"
        return self._get(url)

    def short_interest(self):
        url = f"{BASE_URL}/short_interest"
        return self._get(url)

    def low_float(self):
        url = f"{BASE_URL}/low_float"
        return self._get(url)

    def earnings_calendar(self, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        url = f"{BASE_URL}/earnings_calendar/?date_from={date_from}&date_to={date_to}"
        return self._get(url)

    def ipo_calendar(self):
        url = f"{BASE_URL}/ipo_calendar"
        return self._get(url)
    
    def reverse_repo(self, days=100):
        url = f"{BASE_URL}/reverse_repo/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def daily_treasury(self, days=100):
        url = f"{BASE_URL}/daily_treasury/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def inflation(self):
        url = f"{BASE_URL}/inflation"
        return self._get(url)

    def retail_sales(self, days=100):
        url = f"{BASE_URL}/retail_sales/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def jobless_claims(self, days=100):
        url = f"{BASE_URL}/initial_jobless_claims/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def market_summary(self, market_type="snp500"):
        url = f"{BASE_URL}/market_summary/?type={market_type}"
        # pd.DataFrame(list(r.json().values())[0])
        return self._get(url)

    def senate(self, name="", ticker="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        url = f"{BASE_URL}/government/senate/?name={name}&ticker={ticker}&date_from={date_from}&date_to={date_to}"
        # pd.DataFrame(data["senate"])
        return self._get(url)

    def house(self, name="", ticker="", state="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        url = f"{BASE_URL}/government/house/?name={name}&ticker={ticker}&state={state}&" \
              f"date_from={date_from}&date_to={date_to}"
        # pd.DataFrame(data["house"])
        return self._get(url)

    def trading_halts(self):
        url = f"{BASE_URL}/trading_halts"
        return self._get(url)

    def market_news(self):
        url = f"{BASE_URL}/market_news"
        return self._get(url)
    
    def subreddit(self, ticker="GME", days=30):
        url = f"{BASE_URL}/subreddit_count/{ticker}/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def wsb_mentions(self, ticker="", days=1):
        url = f"{BASE_URL}/reddit/wsb/"
        if ticker:
            url += f"{ticker}/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def wsb_options(self, days=1):
        url = f"{BASE_URL}/wsb_options/"
        if days:
            url += f"?days={str(days)}"
        return self._get(url)

    def stocktwits(self, ticker="GME"):
        url = f"{BASE_URL}/stocktwits/{ticker}"
        return self._get(url)
    
    def sec_fillings(self, ticker, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        url = f"{BASE_URL}/sec_fillings/{ticker}/?date_from={date_from}&date_to={date_to}"
        return self._get(url)

    def news_sentiment(self, ticker):
        url = f"{BASE_URL}/news_sentiment/{ticker}"
        return self._get(url)

    def insider_trading(self, ticker="", limit=500, date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        if not ticker:
            url = f"{BASE_URL}/latest_insider/?limit={str(limit)}"
        else:
            url = f"{BASE_URL}/insider_trading/{ticker}/?date_from={date_from}&date_to={date_to}"
        return self._get(url)

    def latest_insider_trading_summary(self):
        url = f"{BASE_URL}/latest_insider_summary"
        return self._get(url)

    def short_volume(self, ticker="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        if not ticker:
            url = f"{BASE_URL}/top_short_volume"
        else:
            url = f"{BASE_URL}/short_volume/{ticker}/?date_from={date_from}&date_to={date_to}"
        return self._get(url)

    def ftd(self, ticker="", date_from="1999-01-01", date_to=str(datetime.utcnow().date())):
        if not ticker:
            url = f"{BASE_URL}/top_failure_to_deliver"
        else:
            url = f"{BASE_URL}/failure_to_deliver/{ticker}/?date_from={date_from}&date_to={date_to}"
        return self._get(url)

    def borrowed_shares(self, ticker="AAPL"):
        url = f"{BASE_URL}/borrowed_shares/{ticker}"
        return self._get(url)
