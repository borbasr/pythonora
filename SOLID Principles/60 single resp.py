class Invoice:
    def __init__(self, items):
        self.items = items

    def calculate_total(self):
        return sum(item.price for item in self.items)

class InvoiceDisplay:
    def print(self, invoice):
        print(invoice.calculate_total())
