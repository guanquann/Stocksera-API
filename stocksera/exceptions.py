class StockseraRequestException(Exception):
    def __init__(self):
        super(StockseraRequestException, self).__init__()
        self.message = "Invalid API Key / Authorization Headers is empty. " \
                       "Sign up for free at https://stocksera.pythonanywhere.com/accounts/login to receive " \
                       "your free API Key."

    def __str__(self):
        return "StockseraRequestException: {}".format(self.message)