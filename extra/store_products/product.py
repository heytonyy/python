import uuid

class Product:
    def __init__(self, name, price, category) -> None:
        self.name = name
        self.price = price
        self.category = category
        self.id = uuid.uuid4().hex[:8]
        # print(self.id)
    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change
        return self
    def print_info(self):
        print(f"Name: {self.name}\nCategory: {self.category}\nPrice: {self.price} gold")
