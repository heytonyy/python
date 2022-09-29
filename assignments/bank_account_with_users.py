class BankAccount:

    def __init__(self, account_name, int_rate, balance):
        self.account_name = account_name
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self, account_name):
        return f"{account_name} Balance: ${self.balance}"
    
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []
    
    def add_account(self, account_name):
        account = BankAccount(account_name, int_rate=0.02, balance=0)
        self.accounts.append(account)

    def make_deposit(self, name, amount):
        for account in self.accounts:
            if account.account_name == name:
                account.deposit(amount)

    def make_withdrawal(self, name, amount):
        for account in self.accounts:
            if account.account_name == name:
                account.withdraw(amount)

    def transfer_money(self, ammount, other_user, origin_account_name, destination_account_name):
        self.make_withdrawal(origin_account_name, ammount)
        other_user.make_deposit(destination_account_name, ammount)

    def display_user_balance(self):
        for account in self.accounts:
            print(f"User: {self.name}, {account.display_account_info(account.account_name)}")
        return "----" # how to i not print/return anything? i am returning this string just so it doesnt say "None"
######
######
tonys_account = User("Tony", "tonyemail@gmail.com")
tonys_account.add_account("Checking")
tonys_account.add_account("Saving")

tonys_account.make_deposit("Checking", 1000)
tonys_account.make_withdrawal("Checking", 50)
tonys_account.make_deposit("Saving", 1000)

trevs_account = User("Trevor", "trevoremail@gmail.com")
trevs_account.add_account("Checking")
trevs_account.add_account("Saving")

trevs_account.make_deposit("Checking", 1000)
trevs_account.make_withdrawal("Checking", 300)
trevs_account.make_deposit("Saving", 500)

print("Starting Balances:")
tonys_account.display_user_balance()
trevs_account.display_user_balance()

tonys_account.transfer_money(100, trevs_account, "Checking", "Checking")

print("Ending Balances:")
tonys_account.display_user_balance()
trevs_account.display_user_balance()