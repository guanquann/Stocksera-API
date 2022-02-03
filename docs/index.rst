Stockera API
=============
This is the official API for Stocksera. Visit Stocksera at https://stocksera.pythonanywhere.com.

Installation
=============

The package can easily be installed in your terminal by entering

.. code-block::

   pip install stocksera

Import the package
==================

.. code-block::

   import stocksera

Get data from Reddit
=====================

.. code-block::

   reddit = stocksera.Reddit()

   # Get total number of mentions on wallstreetbets
   df = reddit.wsb_mentions(days=1)

   # Get number of mentions of a stock overtime on wallstreetbets
   df = reddit.wsb_mentions(ticker="AAPL")

   # Get total number of puts/calls mentions on wallstreetbets
   df = reddit.wsb_options(days=1)

   # Get number of puts/calls mentions of a stock overtime on wallstreetbets
   df = reddit.wsb_options(ticker="AAPL")

   # Get subreddit count on Reddit
   df = reddit.subreddit(ticker="GME")

Get stocks related data
========================

.. code-block::

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

Get government trades data
===========================

.. code-block::

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
   df = government.house(name="Hon. Nancy Pelosi")

   # Get house trades of a specific ticker
   df = government.house(ticker="AAPL")

Get Economic Data
==================

.. code-block::

   government = stocksera.Economy()

   # Get reverse repo
   df = government.reverse_repo()

   # Get daily treasury
   df = government.daily_treasury()

   # Get inflation
   df = government.inflation()

   # Get initial jobless claims
   df = government.jobless_claims()

   # Get retail sales
   df = government.retail_sales()