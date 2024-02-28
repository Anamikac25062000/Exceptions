# 10)Write a Python program that simulates a banking system. Implement a class called BankAccount with methods to initialize an account with a starting balance, withdraw funds, and handle a custom exception called NegativeBalanceError when the account balance goes below zero.


class NegativeBalanceError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if self.balance - amount < 0:
            raise NegativeBalanceError("Withdrawal amount exceeds the available balance.")
        self.balance -= amount
        return amount

try:
    account = BankAccount(1000)

    withdrawn_amount = account.withdraw(500)
    print(f"Withdrawal successful. Withdrawn amount: ${withdrawn_amount}")
    print(f"Remaining balance: ${account.balance}")

    withdrawn_amount = account.withdraw(700)
    print(f"Withdrawal successful. Withdrawn amount: ${withdrawn_amount}")
    print(f"Remaining balance: ${account.balance}")

except ValueError as ve:
    print(f"Error: {ve}")
except NegativeBalanceError as nbe:
    print(f"Error: {nbe}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
