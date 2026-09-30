"""MenuItem and Menu classes."""


class MenuItem:
    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self._items = {}

    def add_item(self, item):
        self._items[item.number] = item

    def get_item(self, number):
        return self._items.get(number)

    def has_item(self, number):
        return number in self._items

    def display(self):
        print("\n" + "=" * 50)
        print("             FAST BITES RESTAURANT")
        print("=" * 50)
        print(f"{'No.':<5}{'Item':<25}{'Price':>10}")
        print("-" * 50)

        for item in self._items.values():
            print(f"{item.number:<5}{item.name:<25}₱{item.price:>8.2f}")

        print("=" * 50)

    @classmethod
    def default_menu(cls):
        menu = cls()
        data = [
            (1, "Burger", 75.00),
            (2, "Cheeseburger", 95.00),
            (3, "Chicken Meal", 120.00),
            (4, "French Fries", 60.00),
            (5, "Spaghetti", 100.00),
            (6, "Pizza", 150.00),
            (7, "Iced Tea", 40.00),
            (8, "Soft Drink", 35.00),
        ]
        for number, name, price in data:
            menu.add_item(MenuItem(number, name, price))
        return menu
