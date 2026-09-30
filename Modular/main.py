"""Fast Bites Restaurant - Modular version (entry point)."""

from menu import display_menu
from user_input import ask_to_order
from order import take_order
from receipt import print_receipt


def main():
    print("\n" + "=" * 50)
    print("       WELCOME TO FAST BITES RESTAURANT")
    print("=" * 50)

    display_menu()

    if not ask_to_order():
        print("\nThank you for visiting Fast Bites Restaurant!")
        print("Have a great day!")
        return

    orders = take_order()

    if len(orders) == 0:
        print("\nNo orders were placed.")
        print("Thank you for visiting Fast Bites Restaurant!")
        return

    print_receipt(orders)


if __name__ == "__main__":
    main()
