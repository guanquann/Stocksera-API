# Stocksera API

[![Downloads](https://pepy.tech/badge/stocksera)](https://pepy.tech/project/stocksera)

This is the official API for Stocksera. Visit Stocksera at https://github.com/guanquann/Stocksera. 
Sign up for free Stocksera API at https://stocksera.pythonanywhere.com/accounts/developers.

### Installation
The package can easily be installed in your terminal by entering
```
pip install stocksera
```

### Import the package
```
import stocksera

# Sign up for free Stocksera API at https://stocksera.pythonanywhere.com/accounts/developers/
client = stocksera.Client(api_key="YOUR API KEY")
```

### Get data from social media

##### Get total mentions/ mentions of a stock on wallstreetbets
```
data = client.wsb_mentions(days=1, ticker="AAPL")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 1       | number days ago |
| ticker  | No       |         | stock symbol    |

##### Get total number of puts/calls mentions on wallstreetbets
```
data = client.wsb_options(days=1)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 1       | number days ago |

##### Get subreddit count on Reddit
```
data = client.subreddit(days=50, ticker="GME")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |
| ticker  | Yes      | GME     | stock symbol    |

##### Get current trending stocks/ ranking and watchlist count of a stock in stocktwits
```
data = client.stocktwits(ticker="AAPL")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| ticker  | No       |         | stock symbol    |

### Get stocks related data

##### Get SEC fillings of a stock
```
data = client.sec_fillings(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | Yes      | AAPL    | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get news sentiment of a stock
```
data = client.news_sentiment(ticker="AAPL")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| ticker  | Yes      | AAPL    | stock symbol    |

##### Get recent insider trading of all tickers/ insider trading of a stock
```
data = client.insider_trading(limit=500, ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```

| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| limit     | No       | 500     | last n records  |
| ticker    | No       | AAPL    | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get recent insider trading analysis
```
data = client.latest_insider_trading_summary()
```

##### Get stocks with high short volume/ short volume of a stock
```
data = client.short_volume(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get stocks with consistently high FTD/ FTD of a stock
```
data = client.ftd(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get number of shares available and borrow fees of a stock
```
data = client.borrowed_shares(ticker="AAPL")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       | AAPL    | stock symbol    |

### Get government trades data

#### Get all senate trades/ trades of a specific person/ trades of a specific ticker
```
data = client.senate(ticker="AAPL", name="Thomas H Tuberville", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| name      | No       |         | name of person  |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

#### Get all house trades/ trades of a specific person/ trades of a specific ticker
```
data = client.house(ticker="AAPL", name="Nancy Pelosi", state="CA", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| name      | No       |         | name of person  |
| state     | No       |         | district code   |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

### Get ETF data

##### Get market indices
```
data = client.market_summary(market_type="snp500")
```
| Params       | Required | Default | Description              |
| -------      | -------- | ------- | -------------------------|
| market_type  | Yes      | snp500  | snp500/nasdaq100/dia/wsb |

### Get economic data

##### Get reverse repo
```
data = client.reverse_repo(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

##### Get daily treasury
```
data = client.daily_treasury(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

##### Get inflation
```
data = client.inflation()
```

##### Get initial jobless claims
```
data = client.jobless_claims(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

##### Get retail sales
```
data = client.retail_sales(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

### Get stock related news

##### Get recent market news
```
data = client.market_news()
```

##### Get trading halts
```
data = client.trading_halts()
```

### Get other interesting data

##### Get Jim Cramer trades
```
data = client.jim_cramer(ticker="AAPL", segment="featured", call="buy")
```

| Params  | Required | Default | Description                        |
| ------- | -------- | ------- | ---------------------------------- |
| ticker  | No       | all     | stock symbol                       |
| segment | No       | all     | featured/discussed/lightning/guest |
| call    | No       | all     | buy/positive/hold/negative/sell    |

##### Get stocks with high short interest
```
data = client.short_interest()
```

##### Get stocks with low float
```
data = client.low_float()
```

##### Get upcoming and past IPOs
```
data = client.ipo_calendar()
```

##### Get earnings calendar of stocks
```
data = client.earnings_calendar(date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |
