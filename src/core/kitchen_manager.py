import heapq
from stations.grill_station import GrillStation
from stations.fry_station import FryStation
from stations.prep_station import PrepStation
from .menu import Menu

class KitchenManager:
    def __init__(self):
        self.menu = Menu()
        self.grill = GrillStation()
        self.fry = FryStation()
        self.prep = PrepStation()

        self.priority_queue = []  # heap for rush orders
        self.completed_orders = []

    def place_order(self, order):
        heapq.heappush(self.priority_queue, order)
        print(f"[KitchenManager] Received {order}")

    def route_order(self, order):
        station_type = self.menu.get_station_for_item(order.item_name)

        if station_type == "grill":
            self.grill.add_order(order)
        elif station_type == "fry":
            self.fry.add_order(order)
        elif station_type == "prep":
            self.prep.add_order(order)
        else:
            print(f"[KitchenManager] Unknown item: {order.item_name}")

    def run_step(self):
        # Step 1: route highest priority order
        if self.priority_queue:
            next_order = heapq.heappop(self.priority_queue)
            self.route_order(next_order)

        # Step 2: process each station
        for station in [self.grill, self.fry, self.prep]:
            if station.has_orders():
                finished = station.process_next()
                if finished:
                    self.completed_orders.append(finished)
                    print(f"[KitchenManager] Completed {finished}")
