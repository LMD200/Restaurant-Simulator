from .kitchen_station import KitchenStation

class GrillStation(KitchenStation):
    def __init__(self):
        super().__init__("Grill Station", processing_time=5)

    def process_next(self):
        if not self.queue:
            return None

        order = self.queue.popleft()
        print(f"[Grill Station] Grilling {order.item_name}...")
        return order
