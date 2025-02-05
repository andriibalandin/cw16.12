from abc import ABC, abstractmethod
import datetime
import pickle
import os
# Найскладніша домашка поки щo.
# Навіть концептуально спланувати було трішки складно(правда, більше тому що воно звучить складніше ніж насправді).
# На мою думку, ії треба було давати після вивченя json та pickle, тому що вони тут ідеально підходять(благо я так відклав її).


class OrderItem:
    def __init__(self, product_name, unit_price, quantity):
        self.product_name = product_name
        self.unit_price = unit_price
        self.quantity = quantity

    def total_price(self):
        return self.unit_price * self.quantity



class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, amount):
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, amount):
        discount = amount * (self.percentage / 100)
        return amount - discount


class Order:
    def __init__(self, order_id, discount_strategy=None):
        self.order_id = order_id
        self.items = []
        self.discount_strategy = discount_strategy if discount_strategy else NoDiscount()
        self.created_at = datetime.datetime.now()

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        subtotal = sum(item.total_price() for item in self.items)
        total = self.discount_strategy.apply_discount(subtotal)
        return total


class InvoiceGenerator:
    def generate_invoice(self, order):
        lines = []
        lines.append(f"Invoice for Order #{order.order_id}")
        lines.append(f"Date: {order.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("Items:")
        for item in order.items:  # інформаця для кожного товару
            lines.append(
                f" - {item.product_name}: {item.quantity} x ${item.unit_price:.2f} = ${item.total_price():.2f}")
        subtotal = sum(item.total_price() for item in order.items) # без знижки
        lines.append(f"Subtotal: ${subtotal:.2f}")
        total = order.calculate_total() # зі знижкою
        lines.append(f"Total (after discount): ${total:.2f}")
        return "\n".join(lines)


class OrderManager:
    def __init__(self, filename="orders.pkl"):
        self.filename = filename
        self.orders = self.load_orders()

    def load_orders(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                try:
                    return pickle.load(file)
                except Exception:
                    return {}
        return {}

    def save_orders(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.orders, file)

    def save(self, order):
        self.orders[order.order_id] = order
        self.save_orders()

    def get(self, order_id):
        return self.orders.get(order_id)


class OrderService:
    def __init__(self, manager):
        self.manager = manager
        self.next_order_id = max(manager.orders.keys(), default=0) + 1

    def create_order(self, discount_strategy=None):
        order = Order(self.next_order_id, discount_strategy)
        self.manager.save(order) # збереження
        self.next_order_id += 1
        return order


def main():
    manager = OrderManager("orders.pkl")
    order_service = OrderService(manager)
    invoice_generator = InvoiceGenerator()

    order = order_service.create_order(PercentageDiscount(10))
    order.add_item(OrderItem("Laptop", 1500.00, 1))
    order.add_item(OrderItem("Mouse", 50.00, 2))

    invoice = invoice_generator.generate_invoice(order)
    print(invoice)



main()