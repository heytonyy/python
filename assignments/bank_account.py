class BankAccount:
    all_accounts = []
    
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    
    def yield_interest(self):
        self.balance = self.balance + self.balance * self.int_rate
        return self
    
    @classmethod
    def print_accounts(cls):
        for account in BankAccount.all_accounts:
            account.display_account_info()
        return    

tonys_account = BankAccount(0.1, 400)
trevors_account = BankAccount(0.1, 800)

tonys_account.deposit(100).deposit(50).deposit(300).display_account_info()
trevors_account.deposit(100).deposit(50).withdraw(100).withdraw(50).withdraw(200).withdraw(300).display_account_info()


BankAccount.print_accounts()