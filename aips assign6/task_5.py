class BankAccount:
    # Constructor to initialize account holder name and balance
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
        else:
            print("Deposit amount must be positive!")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ₹{amount:.2f}. Remaining balance: ₹{self.balance:.2f}")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive!")

    # Method to check account balance
    def check_balance(self):
        print(f"Current balance: ₹{self.balance:.2f}")


# Taking input from user
name = input("Enter account holder name: ")
account = BankAccount(name)

# Performing transactions
account.deposit(2000)
account.withdraw(500)
account.check_balance()
