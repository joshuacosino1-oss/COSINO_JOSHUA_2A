"""Receipt class."""


class Receipt:
    def __init__(self, order):
        self.order = order

    def print(self):
        order = self.order

        print("\n")
        print("=" * 65)
        print("                 FAST BITES RESTAURANT")
        print("                      ORDER RECEIPT")
        print("=" * 65)

        print(f"{'Item':<22}{'Qty':>6}{'Price':>12}{'Total':>15}")
        print("-" * 65)

        for item in order.items:
            print(
                f"{item.name:<22}"
                f"{item.quantity:>6}"
                f"₱{item.price:>10.2f}"
                f"₱{item.total:>13.2f}"
            )

        print("-" * 65)
        print(f"{'Subtotal:':<45}₱{order.subtotal:>13.2f}")
        label = f"Discount ({int(order.discount_rate * 100)}%):"
        print(f"{label:<45}₱{order.discount:>13.2f}")
        print("-" * 65)
        print(f"{'TOTAL AMOUNT:':<45}₱{order.final_total:>13.2f}")
        print("=" * 65)
        print("             Thank you for ordering!")
        print("                 Please come again!")
        print("=" * 65)
