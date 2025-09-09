class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <=0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def display_balance(self):
        print(f"{self.owner}'s balance is ", self.balance)


# Test it
account = BankAccount("Alice", 100)
account.deposit(50)   # balance = 150
account.withdraw(70)  # balance = 80

try:
    account.withdraw(100)  # will raise exception
except ValueError as e:
    print("Error:", e)

account.display_balance()  # Alice's balance is 80
