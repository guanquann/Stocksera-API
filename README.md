# Stocksera API

[![Downloads](https://pepy.tech/badge/stocksera)](https://pepy.tech/project/stocksera)

This is the official API for Stocksera. Visit Stocksera at https://github.com/guanquann/Stocksera.

#### Installation
The package can easily be installed in your terminal by entering
```
pip install stocksera
```

#### Import the package
```
import stocksera
```

#### Get data from Reddit
```
reddit = stocksera.Reddit()

# Get total number of mentions on wallstreetbets
df = reddit.wsb_mentions(days=1)

# Get number of mentions of a stock overtime on wallstreetbets
df = reddit.wsb_mentions(days=1, ticker="AAPL")

# Get total number of puts/calls mentions on wallstreetbets
df = reddit.wsb_options(days=1)

# Get subreddit count on Reddit
df = reddit.subreddit(days=50, ticker="GME")
```

#### Get stocks related data
```
stock = stocksera.Stock()

# Get SEC fillings of a stock
df = stock.sec_fillings(ticker="AAPL")

# Get news and sentiment of a stock
df = stock.news_sentiment(ticker="AAPL")

# Get recent insider trading of all tickers
df = stock.insider_trading(limit=500)

# Get insider trading of a stock
df = stock.insider_trading(ticker="AAPL")

# Get recent insider trading analysis
df = stock.latest_insider_trading_summary()

# Get stocks with recent consistenly high FTD
df = stock.ftd()

# Get FTD of a stock
df = stock.ftd(ticker="AAPL")

# Get earnings calendar of stocks
df = stock.earnings_calendar()
```

#### Get government trades data
```
government = stocksera.Government()

# Get all senate trades
df = government.senate()

# Get senate trades of a specific person
df = government.senate(name="Thomas H Tuberville")

# Get senate trades of a specific ticker
df = government.senate(ticker="AAPL")

# Get all house trades
df = government.house()

# Get house trades of a specific person
df = government.house(name="Nancy Pelosi")

# Get house trades of a specific ticker
df = government.house(ticker="AAPL")

# Get house trades of a state
df = government.house(state="TX")
```

#### Get ETF data
```
etf = stocksera.ETF()

# Get market indices
df = etf.market_summary(market_type="snp500")

# Get Jim Cramer trades
df = etf.jim_cramer(ticker="AAPL", segment="featured", call="buy")
```

#### Get economic data
```
economy = stocksera.Economy()

# Get reverse repo
df = economy.reverse_repo(days=100)

# Get daily treasury
df = economy.daily_treasury(days=100)

# Get inflation
df = economy.inflation()

# Get initial jobless claims
df = economy.jobless_claims(days=100)

# Get retail sales
df = economy.retail_sales(days=100)
```