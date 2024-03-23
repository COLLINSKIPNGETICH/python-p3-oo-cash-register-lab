#!/usr/bin/env python3

class CashRegister:
    def __init__(self):
        self.total = 0
        self.discount = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, item, price, quantity=1):
        transaction_amount = price * quantity
        self.items.append({"item": item, "price": price, "quantity": quantity})
        self.total += transaction_amount
        self.last_transaction = transaction_amount

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"Applying a {self.discount}% discount. New total: ${self.total}"
        else:
            return "No discount applied."

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
            return "Last transaction voided."
        else:
            return "No transactions to void."
