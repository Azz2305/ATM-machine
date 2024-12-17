class Account:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        return f"Your balance is: ${self.balance}"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew: ${amount}")
            return "Withdrawal successful."
        return "Insufficient funds."

class CashMachine:
    def __init__(self):
        self.accounts = {}

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account.pin == pin:
            return account
        return None

    def menu(self, account):
        while True:
            choice = input("1. Check Balance 2. Deposit 3. Withdraw 4. Transactions 5. Exit: ")
            if choice == "1":
                print(account.check_balance())
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                print(account.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                print(account.withdraw(amount))
            elif choice == "4":
                print("\n".join(account.transactions) if account.transactions else "No transactions yet.")
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")