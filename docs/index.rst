Stockera API
=============
This is the official API for Stocksera. Visit Stocksera at https://github.com/guanquann/Stocksera.

Installation
=============

The package can easily be installed in your terminal by entering

.. code-block:: bash

    pip install stocksera

Import the package
==================

.. code-block::

    import stocksera

Get data from social media
===========================

.. code-block::

    social = stocksera.Social()

Get total mentions/ mentions of a stock on wallstreetbets
**********************************************************

.. code-block::

    df = social.wsb_mentions(days=1, ticker="AAPL")

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 1       | number days ago |
+---------+----------+---------+-----------------+
| ticker  | No       |         | stock symbol    |
+---------+----------+---------+-----------------+

Get total number of puts/calls mentions on wallstreetbets
***********************************************************

.. code-block::

    df = social.wsb_options(days=1)


+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 1       | number days ago |
+---------+----------+---------+-----------------+

Get subreddit count on Reddit
******************************

.. code-block::

    df = social.subreddit(days=50, ticker="GME")

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 100     | number days ago |
+---------+----------+---------+-----------------+
| ticker  | Yes      | GME     | stock symbol    |
+---------+----------+---------+-----------------+

Get current trending stocks/ ranking and watchlist count of a stock in stocktwits
***********************************************************************************

.. code-block::

    df = social.stocktwits(ticker="AAPL")

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| ticker  | No       |         | stock symbol    |
+---------+----------+---------+-----------------+

Get stocks related data
========================

.. code-block::

    stock = stocksera.Stock()

Get SEC fillings of a stock
****************************

.. code-block::

    df = stock.sec_fillings(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| ticker    | Yes      | AAPL    | stock symbol    |
+-----------+----------+---------+-----------------+
| date_from | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+
| date_to   | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+

Get news sentiment of a stock
*******************************

.. code-block::

    df = stock.news_sentiment(ticker="AAPL")

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| ticker  | Yes      | AAPL    | stock symbol    |
+---------+----------+---------+-----------------+

Get recent insider trading of all tickers/ insider trading of a stock
**********************************************************************

.. code-block::

    df = stock.insider_trading(limit=500, ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| limit     | No       | 500     | last n records  |
+-----------+----------+---------+-----------------+
| ticker    | No       | AAPL    | number days ago |
+-----------+----------+---------+-----------------+
| date_from | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+
| date_to   | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+

Get recent insider trading analysis
************************************

.. code-block::

    df = stock.latest_insider_trading_summary()

Get stocks with high short volume/ short volume of a stock
***********************************************************

.. code-block::

    df = stock.short_volume(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| ticker    | No       |         | stock symbol    |
+-----------+----------+---------+-----------------+
| date_from | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+
| date_to   | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+

Get stocks with consistently high FTD/ FTD of a stock
******************************************************

.. code-block::

    df = stock.ftd(ticker="AAPL", date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| ticker    | No       |         | stock symbol    |
+-----------+----------+---------+-----------------+
| date_from | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+
| date_to   | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+

Get number of shares available and borrow fees of a stock
**********************************************************

.. code-block::

    df = stock.borrowed_shares(ticker="AAPL")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| ticker    | No       | AAPL    | stock symbol    |
+-----------+----------+---------+-----------------+

Get government trades data
===========================

.. code-block::

    government = stocksera.Government()

Get all senate trades/ trades of a specific person/ trades of a specific ticker
********************************************************************************

.. code-block::

    df = government.senate(ticker="AAPL", name="Thomas H Tuberville", date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| ticker    | No       |         | stock symbol    |
+-----------+----------+---------+-----------------+
| name      | No       |         | name of person  |
+-----------+----------+---------+-----------------+
| date_from | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+
| date_to   | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+

Get all house trades/ trades of a specific person/ trades of a specific ticker
********************************************************************************

.. code-block::

    df = government.house(ticker="AAPL", name="Nancy Pelosi", state="CA", date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+---------------------------+
| Params    | Required | Default | Description               |
+===========+==========+=========+===========================+
| ticker    | No       |         | stock symbol              |
+-----------+----------+---------+---------------------------+
| name      | No       |         | name of person            |
+-----------+----------+---------+---------------------------+
| state     | No       |         | 2 character district code |
+-----------+----------+---------+---------------------------+
| date_from | No       |         | YYYY-MM-DD                |
+-----------+----------+---------+---------------------------+
| date_to   | No       |         | YYYY-MM-DD                |
+-----------+----------+---------+---------------------------+

Get ETF data
==================

.. code-block::

    etf = stocksera.ETF()

Get market indices
*******************

.. code-block::

    df = etf.market_summary(market_type="snp500")

+--------------+----------+---------+--------------------------+
| Params       | Required | Default | Description              |
+==============+==========+=========+==========================+
| market_type  | Yes      | snp500  | snp500/nasdaq100/dia/wsb |
+--------------+----------+---------+--------------------------+

Get economic data
==================

.. code-block::

    economy = stocksera.Economy()

Get reverse repo
*****************

.. code-block::

    df = economy.reverse_repo(days=100)

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 100     | number days ago |
+---------+----------+---------+-----------------+

Get daily treasury
*******************

.. code-block::

    df = economy.daily_treasury(days=100)

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 100     | number days ago |
+---------+----------+---------+-----------------+

Get inflation
**************

.. code-block::

    df = economy.inflation()

Get initial jobless claims
***************************

.. code-block::

    df = economy.jobless_claims(days=100)

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 100     | number days ago |
+---------+----------+---------+-----------------+

Get retail sales
*****************

.. code-block::

    df = economy.retail_sales(days=100)

+---------+----------+---------+-----------------+
| Params  | Required | Default | Description     |
+=========+==========+=========+=================+
| days    | No       | 100     | number days ago |
+---------+----------+---------+-----------------+

Get stock related news
=======================

.. code-block::

    news = stocksera.News()

Get recent market news
***********************

.. code-block::

    df = news.market_news()

Get trading halts
******************

.. code-block::

    df = news.trading_halts()

Get other interesting data
===========================

.. code-block::

    discover = stocksera.Discover()

Get Jim Cramer trades
**********************

.. code-block::

    df = discover.jim_cramer(ticker="AAPL", segment="featured", call="buy")

+---------+----------+---------+------------------------------------+
| Params  | Required | Default | Description                        |
+=========+==========+=========+====================================+
| ticker  | No       | all     | stock symbol                       |
+---------+----------+---------+------------------------------------+
| segment | No       | all     | featured/discussed/lightning/guest |
+---------+----------+---------+------------------------------------+
| call    | No       | all     | buy/positive/hold/negative/sell    |
+---------+----------+---------+------------------------------------+

Get stocks with high short interest
************************************

.. code-block::

    df = discover.short_interest()

Get stocks with low float
***************************

.. code-block::

    df = discover.low_float()


Get upcoming and past IPOs
****************************

.. code-block::

    df = discover.ipo_calendar()


Get earnings calendar of stocks
********************************

.. code-block::

    df = discover.earnings_calendar(date_from="2022-01-01", date_to="2022-01-31")

+-----------+----------+---------+-----------------+
| Params    | Required | Default | Description     |
+===========+==========+=========+=================+
| date_from | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+
| date_to   | No       |         | YYYY-MM-DD      |
+-----------+----------+---------+-----------------+