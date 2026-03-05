import threading
from orderbook_models import OrderNode, PriceLevelList

class OrderBook:
    def __init__(self, symbol):
        self.symbol = symbol

        # this is a hashmap. the key = price, value = PriceLevelList(DLL)
        self.bids = {} #buy
        self.asks = {} #sell

        # Threading Lock: Critical for high-performance pipelines.
        # Prevents the WebSocket thread and the UI thread from 
        # accessing the DLL pointers at the exact same microsecond.
        self.lock = threading.Lock()