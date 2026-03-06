import threading
from orderbook_models import OrderNode, PriceLevelList

# Hashmap/ dictionary 
# provides instant lookup by order_id
class OrderBook:
    def __init__(self, symbol):
        self.symbol = symbol

        # this is a hashmap. the key = price, value = PriceLevelList(DLL)
        self.bids = {} #BUY
        self.asks = {} #SELL

        # this is so we can find the node
        self.order_map = {}
        # Threading Lock: Critical for high-performance pipelines.
        # Prevents the WebSocket thread and the UI thread from accessing the DLL pointers at the exact same microsecond.
        self.lock = threading.Lock()

    def add_order(self, order_id, price, quantity, user_id, side):
        """create new ordernode and add to back of dll so it follows in the que"""

        new_node = OrderNode(order_id, price, quantity, user_id, side)

        with self.lock:
            # store in map so we can find it instantly 
            self.order_map[order_id] = new_node

            # determine if we are adding to bids or asks
            if side == 'BUY':
                target_map = self.bids
            else:
                target_map = self.asks

            # check if price level exists, if not create new DLL and add order to it
            if price not in target_map:
                target_map[price] = PriceLevelList()
            # append to the end of the DLL queue
            target_map[price].append(new_node)

    def cancel_order(self, order_id):
        """cancel order and if its in middle of que, it points to the next node closer to head 
        and tells its previous to point at it instead"""

        with self.lock:
            # failsafe to check if its in the map or print error
            if order_id not in self.order_map:
                print(f"{order_id} not found")
                return
            
            node_to_remove = self.order_map[order_id]
            price = node_to_remove.price
            side = node_to_remove.side

            # which side is the node on
            if side == 'BUY':
                target_map = self.bids
            else:
                target_map = self.asks

            # remove it
            target_map[price].remove(node_to_remove)
            del self.order_map[order_id]