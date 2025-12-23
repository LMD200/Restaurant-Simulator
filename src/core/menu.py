class Menu:
    def __init__(self):
        self.routes = {
            "burger": "grill",
            "steak": "grill",
            "fries": "fry",
            "wings": "fry",
            "salad": "prep",
            "sandwich": "prep"
        }

    def get_station_for_item(self, item_name):
        return self.routes.get(item_name, None)
