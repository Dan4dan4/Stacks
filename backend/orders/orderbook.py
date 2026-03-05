import threading
from orderbook_models import OrderNode, PriceLevelList

# Hashmap/ dictionary
class OrderBook:
    def __init__(self, symbol):
        self.symbol = symbol

        # this is a hashmap. the key = price, value = PriceLevelList(DLL)
        self.bids = {} #BUY
        self.asks = {} #SELL

        # Threading Lock: Critical for high-performance pipelines.
        # Prevents the WebSocket thread and the UI thread from 
        # accessing the DLL pointers at the exact same microsecond.
        self.lock = threading.Lock()

    def add_order(self, order_id, price, quantity, user_id, side):
        """create new ordernode and add to back of dll"""

        new_node = OrderNode(order_id, price, quantity, user_id, side)

        with self.lock:
            # determine if we are adding to bids or asks
            if side == 'BUY':
                target_map = self.bids
            else:
                target_map = self.asks

            # check if price level exists, if not create new DLL and add order to it
            if price not in target_map:
                target_map[price] = PriceLevelList()
            target_map[price].append(new_node)