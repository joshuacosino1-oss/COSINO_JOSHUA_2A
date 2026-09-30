"""OrderItem and Order classes."""


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.name = menu_item.name
        self.price = menu_item.price
        self.quantity = quantity

    @property
    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, order_item):
        self.items.append(order_item)

    def is_empty(self):
        return len(self.items) == 0

    @property
    def subtotal(self):
        return sum(item.total for item in self.items)

    @property
    def discount_rate(self):
        if self.subtotal >= 1000:
            return 0.10
        elif self.subtotal >= 500:
            return 0.05
        return 0.00

    @property
    def discount(self):
        return self.subtotal * self.discount_rate

    @property
    def final_total(self):
        return self.subtotal - self.discount
