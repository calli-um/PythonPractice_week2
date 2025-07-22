# Parent Class "BankAccount"
class BankAccount:
    def __init__(self, owner, balance):
        self.acc_owner = owner
        self.acc_balance = float(balance)
        self.history = [f"Account created for {self.acc_owner} with balance ${self.acc_balance:.2f}"]

    def deposit(self, amount):
        amount = float(amount)
        if amount > 0:
            self.acc_balance += amount
            self.history.append(f"Deposited ${amount:.2f}")
        else:
            raise ValueError("Amount must be a positive number.")

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.acc_balance:
            self.acc_balance -= amount
            self.history.append(f"Withdrew ${amount:.2f}")
        elif amount <= 0:
            raise ValueError("Amount must be a positive number.")
        else:
            raise ValueError("Insufficient Balance")

    def get_balance(self):
        return self.acc_balance

    def __str__(self):
        return f"{self.acc_owner}'s account | balance: ${self.acc_balance:.2f}"


# Child Class "SavingsAccount"
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = float(interest_rate)

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if self.acc_balance - amount < 50:
            raise ValueError("Savings Account must maintain a minimum balance of $50")
        super().withdraw(amount)

    def apply_interest(self):
        interest = self.acc_balance * self.interest_rate / 100
        self.acc_balance += interest
        self.history.append(f"Interest Applied PKR {interest:.2f}")
