from collections import deque
from abc import ABC, abstractmethod

class KitchenStation(ABC):
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.queue = deque()  # FIFO queue

    def add_order(self, order):
        self.queue.append(order)
        print(f"[{self.name}] Added {order}")

    @abstractmethod
    def process_next(self):
        pass

    def has_orders(self):
        return len(self.queue) > 0