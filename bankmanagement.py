class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def display_balance(self):
        print(f"Account Balance for {self.account_holder}: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into {self.account_holder}'s account.")
            self.display_balance()
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from {self.account_holder}'s account.")
            self.display_balance()
        else:
            print("Invalid withdrawal amount or insufficient funds.")

if __name__ == "__main__":
    # Getting user input for account details
    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance (if any): "))

    # Creating a new account
    account = BankAccount(account_holder, initial_balance)

    while True:
        # Displaying options to the user
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Make a Deposit")
        print("3. Make a Withdrawal")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            account.display_balance()
        elif choice == "2":
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
