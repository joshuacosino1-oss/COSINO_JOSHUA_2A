"""Order-taking and price computation."""

from menu import menu, display_menu
from user_input import get_quantity, ask_order_another


def take_order():
    orders = []

    while True:
        display_menu()

        try:
            choice = int(input("Enter the item number: "))

            if choice not in menu:
                print("Invalid item number. Please choose from the menu.")
                continue

            quantity = get_quantity()

            item_name = menu[choice]["name"]
            item_price = menu[choice]["price"]
            total_price = item_price * quantity

            orders.append({
                "name": item_name,
                "price": item_price,
                "quantity": quantity,
                "total": total_price,
            })

            print(f"\nAdded: {quantity} x {item_name}")
            print(f"Item Total: ₱{total_price:.2f}")

        except ValueError:
            print("Invalid input. Please enter a number.")

        if not ask_order_another():
            return orders


def calculate_total(orders):
    subtotal = sum(order["total"] for order in orders)

    if subtotal >= 1000:
        discount_rate = 0.10
    elif subtotal >= 500:
        discount_rate = 0.05
    else:
        discount_rate = 0.00

    discount = subtotal * discount_rate
    final_total = subtotal - discount

    return subtotal, discount_rate, discount, final_total
