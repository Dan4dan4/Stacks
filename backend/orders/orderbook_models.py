import time


class OrderNode:
    """
    represents a single ORDER or "tick
    """
    def __init__(self, order_id, price, quantity, user_id, side):
        self.order_id = order_id
        self.price = price
        self.quantity = quantity
        self.user_id = user_id
        # buy side or sell side
        self.side = side

        # pointers for the doubly linkedlist
        self.next = None
        self.prev = None


class PriceLevelList:
    """
    represents all orders at a specific price. this is going to create a forest of Doubly linked lists, 
    every diff price level for bids and asks is going to hav their own DLL.
    """
    def __init__(self):

        self.head= None
        self.tail = None
        self.total_volume = 0