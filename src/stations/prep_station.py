from .kitchen_station import KitchenStation

class PrepStation(KitchenStation):
    def __init__(self):
        super().__init__("Prep Station", processing_time=1)

    def process_next(self):
        if not self.queue:
            return None

        order = self.queue.popleft()
        print(f"[Prep Station] Preparing {order.item_name}...")
        return order
