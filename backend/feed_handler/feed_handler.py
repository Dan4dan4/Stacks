from orders.orderbook import OrderBook

class FeedHandler:
    def __init__(self, api_key, symbols):
        self.api_key= api_key
        self.symbols = symbols

        self.url = "wss://delayed.massive.com/stocks"
        self.books = {s: OrderBook(s) for s in symbols}