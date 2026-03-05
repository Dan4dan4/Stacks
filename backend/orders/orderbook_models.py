import time

# represents a single tick or Order
class OrderNode:
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