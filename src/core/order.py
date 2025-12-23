class Order:
    def __init__(self, order_id, item_name, priority=1):
        self.order_id = order_id
        self.item_name = item_name
        self.priority = priority  # lower = higher priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Order#{self.order_id}({self.item_name}, priority={self.priority})"
