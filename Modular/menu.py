"""Menu data and menu display."""

menu = {
    1: {"name": "Burger", "price": 75.00},
    2: {"name": "Cheeseburger", "price": 95.00},
    3: {"name": "Chicken Meal", "price": 120.00},
    4: {"name": "French Fries", "price": 60.00},
    5: {"name": "Spaghetti", "price": 100.00},
    6: {"name": "Pizza", "price": 150.00},
    7: {"name": "Iced Tea", "price": 40.00},
    8: {"name": "Soft Drink", "price": 35.00},
}


def display_menu():
    print("\n" + "=" * 50)
    print("             FAST BITES RESTAURANT")
    print("=" * 50)
    print(f"{'No.':<5}{'Item':<25}{'Price':>10}")
    print("-" * 50)

    for number, item in menu.items():
        print(f"{number:<5}{item['name']:<25}₱{item['price']:>8.2f}")

    print("=" * 50)
