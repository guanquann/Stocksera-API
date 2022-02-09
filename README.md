# Stocksera API

[![Downloads](https://pepy.tech/badge/stocksera)](https://pepy.tech/project/stocksera)

This is the official API for Stocksera. Visit Stocksera at https://github.com/guanquann/Stocksera.

### Installation
The package can easily be installed in your terminal by entering
```
pip install stocksera
```

### Import the package
```
import stocksera
```

### Get data from social media
```
social = stocksera.Social()
```

##### Get total mentions/ mentions of a stock on wallstreetbets
```
df = social.wsb_mentions(days=1, ticker="AAPL")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 1       | number days ago |
| ticker  | No       |         | stock symbol    |

##### Get total number of puts/calls mentions on wallstreetbets
```
df = social.wsb_options(days=1)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 1       | number days ago |

##### Get subreddit count on Reddit
```
df = social.subreddit(days=50, ticker="GME")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |
| ticker  | Yes      | GME     | stock symbol    |

##### Get current trending stocks/ ranking and watchlist count of a stock in stocktwits
```
df = social.stocktwits(ticker="AAPL")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| ticker  | No       |         | stock symbol    |

### Get stocks related data
```
stock = stocksera.Stock()
```

##### Get SEC fillings of a stock
```
df = stock.sec_fillings(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | Yes      | AAPL    | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get news sentiment of a stock
```
df = stock.news_sentiment(ticker="AAPL")
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| ticker  | Yes      | AAPL    | stock symbol    |

##### Get recent insider trading of all tickers/ insider trading of a stock
```
df = stock.insider_trading(limit=500, ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```

| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| limit     | No       | 500     | last n records  |
| ticker    | No       | AAPL    | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get recent insider trading analysis
```
df = stock.latest_insider_trading_summary()
```

##### Get stocks with high short volume/ short volume of a stock
```
df = stock.short_volume(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get stocks with consistently high FTD/ FTD of a stock
```
df = stock.ftd(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

##### Get earnings calendar of stocks
```
df = stock.earnings_calendar(date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

### Get government trades data
```
government = stocksera.Government()
```

#### Get all senate trades/ trades of a specific person/ trades of a specific ticker
```
df = government.senate(ticker="AAPL", name="Thomas H Tuberville", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| name      | No       |         | name of person  |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

#### Get all house trades/ trades of a specific person/ trades of a specific ticker
```
df = government.house(ticker="AAPL", name="Nancy Pelosi", state="CA", date_from="2022-01-01", date_to="2022-01-31")
```
| Params    | Required | Default | Description     |
| --------- | -------- | ------- | --------------- |
| ticker    | No       |         | stock symbol    |
| name      | No       |         | name of person  |
| state     | No       |         | district code   |
| date_from | No       |         | YYYY-MM-DD      |
| date_to   | No       |         | YYYY-MM-DD      |

### Get ETF data
```
etf = stocksera.ETF()
```

##### Get market indices
```
df = etf.market_summary(market_type="snp500")
```
| Params       | Required | Default | Description              |
| -------      | -------- | ------- | -------------------------|
| market_type  | Yes      | snp500  | snp500/nasdaq100/dia/wsb |


##### Get Jim Cramer trades
```
df = etf.jim_cramer(ticker="AAPL", segment="featured", call="buy")
```

| Params  | Required | Default | Description                                              |
| ------- | -------- | ------- | ---------------------------------- |
| ticker  | No       | all     | stock symbol                       |
| segment | No       | all     | featured/discussed/lightning/guest |
| call    | No       | all     | buy/positive/hold/negative/sell    |

### Get economic data
```
economy = stocksera.Economy()
```

##### Get reverse repo
```
df = economy.reverse_repo(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

##### Get daily treasury
```
df = economy.daily_treasury(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

##### Get inflation
```
df = economy.inflation()
```

##### Get initial jobless claims
```
df = economy.jobless_claims(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |

##### Get retail sales
```
df = economy.retail_sales(days=100)
```
| Params  | Required | Default | Description     |
| ------- | -------- | ------- | --------------- |
| days    | No       | 100     | number days ago |
