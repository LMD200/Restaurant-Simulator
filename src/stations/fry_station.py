from .kitchen_station import KitchenStation

class FryStation(KitchenStation):
    def __init__(self):
        super().__init__("Fry Station", processing_time=3)

    def process_next(self):
        if not self.queue:
            return None

        order = self.queue.popleft()
        print(f"[Fry Station] Frying {order.item_name}...")
        return order
