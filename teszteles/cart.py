class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def get_total_items(self):
        return sum(self.items.values())
