from dataclasses import dataclass

@dataclass
class BankAccount:
    id: int
    balance:int = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True