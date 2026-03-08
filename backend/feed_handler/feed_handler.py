from orders.orderbook import OrderBook

class FeedHandler:
    def __init__(self, api_key, symbols):
        self.api_key= api_key
        self.symbols = symbols

        self.url = "wss://delayed.massive.com/stocks"

        # creates the forest of orderbooks, using a dictionary because we WONT be foresting all stocks from this websocket
        # we will populate the dictionary and use it for this specific demo
        self.books = {s: OrderBook(s) for s in symbols}