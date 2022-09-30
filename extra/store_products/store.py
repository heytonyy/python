class Store:
    def __init__(self, name) -> None:
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
    def sell_product(self, id):
        for item in self.products:
            if id == item.id:
                print("Sellling...")
                print(f"    Name: {item.name}\n    Category: {item.category}\n    Price: {item.price}")
                self.products.remove(item)
    def inflation(self, percent_increase):
        for item in self.products:
            item.update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for item in self.products:
            if item.category == category:
                item.update_price(percent_discount, False)