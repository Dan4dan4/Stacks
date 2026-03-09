from orders.orderbook import OrderBook
from massive import WebSocketClient
from massive.websocket.models import WebSocketMessage

class FeedHandler:
    def __init__(self, api_key, symbols):
        self.api_key= api_key
        self.symbols = symbols

        # FOLLOWING MASSIVE GITHUB DOCS FOR WEBSOCKET CLIENT SETUP
        
        # creates the forest of orderbooks, using a dictionary because we WONT be foresting all stocks from this websocket
        # we will populate the dictionary and use it for this specific demo
        self.books = {s: OrderBook(s) for s in symbols}
        
        # we subscribe to Trades (T.TICKER) for each symbol
        subscriptions = [f"T.{s}" for s in symbols]
        self.ws = WebSocketClient(
            api_key=self.api_key, 
            subscriptions=subscriptions
        )
        # point the client to the specific delayed URL from the docs
        self.ws.url = "wss://delayed.massive.com/stocks"