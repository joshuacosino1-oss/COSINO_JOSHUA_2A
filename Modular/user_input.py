"""Functions that read and validate user input."""


def ask_yes_no(prompt):
    """Keep asking until the user answers yes or no. Returns True/False."""
    while True:
        answer = input(prompt).lower().strip()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Invalid input. Please enter yes or no.")


def ask_to_order():
    return ask_yes_no("\nWould you like to order? (yes/no): ")


def ask_order_another():
    return ask_yes_no("\nWould you like to order another item? (yes/no): ")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
