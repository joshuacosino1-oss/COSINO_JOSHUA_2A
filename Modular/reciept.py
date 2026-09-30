"""Receipt printing."""

from order import calculate_total


def print_receipt(orders):
    subtotal, discount_rate, discount, final_total = calculate_total(orders)

    print("\n")
    print("=" * 65)
    print("                 FAST BITES RESTAURANT")
    print("                      ORDER RECEIPT")
    print("=" * 65)

    print(f"{'Item':<22}{'Qty':>6}{'Price':>12}{'Total':>15}")
    print("-" * 65)

    for order in orders:
        print(
            f"{order['name']:<22}"
            f"{order['quantity']:>6}"
            f"₱{order['price']:>10.2f}"
            f"₱{order['total']:>13.2f}"
        )

    print("-" * 65)
    print(f"{'Subtotal:':<45}₱{subtotal:>13.2f}")
    print(f"{'Discount (' + str(int(discount_rate * 100)) + '%):':<45}₱{discount:>13.2f}")
    print("-" * 65)
    print(f"{'TOTAL AMOUNT:':<45}₱{final_total:>13.2f}")
    print("=" * 65)
    print("             Thank you for ordering!")
    print("                 Please come again!")
    print("=" * 65)
