from src.core.order import Order
from src.core.kitchen_manager import KitchenManager

def main():
    kitchen = KitchenManager()

    # Sample orders
    kitchen.place_order(Order(1, "burger", priority=2))
    kitchen.place_order(Order(2, "fries", priority=1))
    kitchen.place_order(Order(3, "salad", priority=3))
    kitchen.place_order(Order(4, "steak", priority=0))  # VIP order

    # Run simulation steps
    for _ in range(10):
        kitchen.run_step()

if __name__ == "__main__":
    main()
