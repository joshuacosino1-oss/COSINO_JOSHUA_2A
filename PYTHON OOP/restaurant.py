"""Restaurant class - controls the whole ordering flow."""

from menu import Menu
from order import Order, OrderItem
from receipt import Receipt


class Restaurant:
    def __init__(self, name="Fast Bites Restaurant"):
        self.name = name
        self.menu = Menu.default_menu()

    # ---------- input helpers ----------
    def _ask_yes_no(self, prompt):
        while True:
            answer = input(prompt).lower().strip()

            if answer in ("yes", "y"):
                return True
            elif answer in ("no", "n"):
                return False
            else:
                print("Invalid input. Please enter yes or no.")

    def _get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

    # ---------- main behaviour ----------
    def take_order(self):
        order = Order()

        while True:
            self.menu.display()

            try:
                choice = int(input("Enter the item number: "))

                if not self.menu.has_item(choice):
                    print("Invalid item number. Please choose from the menu.")
                    continue

                quantity = self._get_quantity()
                order_item = OrderItem(self.menu.get_item(choice), quantity)
                order.add_item(order_item)

                print(f"\nAdded: {quantity} x {order_item.name}")
                print(f"Item Total: ₱{order_item.total:.2f}")

            except ValueError:
                print("Invalid input. Please enter a number.")

            if not self._ask_yes_no("\nWould you like to order another item? (yes/no): "):
                return order

    def run(self):
        print("\n" + "=" * 50)
        print("       WELCOME TO FAST BITES RESTAURANT")
        print("=" * 50)

        self.menu.display()

        if not self._ask_yes_no("\nWould you like to order? (yes/no): "):
            print("\nThank you for visiting Fast Bites Restaurant!")
            print("Have a great day!")
            return

        order = self.take_order()

        if order.is_empty():
            print("\nNo orders were placed.")
            print("Thank you for visiting Fast Bites Restaurant!")
            return

        Receipt(order).print()
