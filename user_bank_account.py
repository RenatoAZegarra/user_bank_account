class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate_precentage, balance = 0): 
        self.balance = balance
        self.int_rate = int_rate_precentage/100
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
    def display_account_info(self):
        print(f"Balance is : {self.balance} Intrest is: {self.int_rate}")
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {}
        self.account = BankAccount(1,100)
    def create_account(self, account_number, int_rate_precentage=2, balance=0):
        if account_number in self.accounts:
            print(f"Account number {account_number} already exists.")
            return
        self.accounts[account_number] = BankAccount(int_rate_precentage, balance)
        print(f"Account number {account_number} created successfully.")
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self, account_number):
        if account_number not in self.accounts:
            print(f"Account number {account_number} does not exist.")
            return
        print(f"Account balance for account number {account_number}: {self.accounts[account_number].balance}")
    def display_account_info(self):
        print(f"Name is : {self.name} Email is: {self.email} Accounts in bank : {self.accounts}")
        self.account.display_account_info()
    def transfer_money(self, from_account_number, to_account_number, amount):
        if from_account_number not in self.accounts:
            print(f"Account number {from_account_number} does not exist.")
            return
        if to_account_number not in self.accounts:
            print(f"Account number {to_account_number} does not exist.")
            return
        if self.accounts[from_account_number].balance < amount:
            print("Insufficient funds.")
            return
        self.accounts[from_account_number].withdraw(amount)
        self.accounts[to_account_number].deposit(amount)
        print(f"${amount} transferred from account number {from_account_number} to account number {to_account_number}.")


user = User("John", "johnsmith@gmail.com")
user.create_account("12345", 2, 1000)
user.create_account("67890", 1)
user.make_deposit(300)
user.make_withdrawl(1000)
user.display_account_info()
user.display_user_balance("12345")

user.transfer_money("12345", "67890", 300)
user.display_user_balance("67890")
