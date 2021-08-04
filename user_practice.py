class BankAccount:
    # don't forget to add some default values for these parameters!
    accounts = []
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if (self.balance > amount):
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Carging a $5 fee")
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= (self.int_rate + 1)
        return self
    @classmethod
    def get_all_info(cls):
        for account in cls.accounts:
            print(f"Your interest rate is: {account.int_rate} Your balance is: {account.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, int_rate, is_roth, balance = 0):
        super().__init__(int_rate, balance)
        self.is_roth = is_roth

class RetirementAccount(BankAccount):
    def __init__(self, int_rate, balance=0):
        super().__init__(int_rate, balance)
    def withdraw(self, amount, is_early):
        if is_early:
            amount = amount * 1.1
        super().withdraw(amount)
        return self

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate = 0.02, balance = 0)

        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value received
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        # print(f"User: {self.name}, Balance: {self.account_balance}")
        self.account.display_account_info()
        return self

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self


zach = User('Zach Kellen', 'zach@codingdojo.com')
kylee = User('Kylee F', 'kyleef@codingdojo.com')
fran = User('Fran M', 'franm@codingdojo.com')

# zach.make_deposit(50)
# zach.make_deposit(100)
# zach.make_deposit(200)
# zach.make_withdrawal(150)
# zach.display_user_balance()

zach.make_deposit(50).make_deposit(100).make_deposit(200).make_withdrawal(150).display_user_balance()

# kylee.make_deposit(200)
# kylee.make_deposit(300)
# kylee.make_withdrawal(100)
# kylee.make_withdrawal(200)
# kylee.display_user_balance()

kylee.make_deposit(200).make_deposit(300).make_withdrawal(100).make_withdrawal(200).display_user_balance()

# fran.make_deposit(1000)
# fran.make_withdrawal(100)
# fran.make_withdrawal(200)
# fran.make_withdrawal(300)
# fran.display_user_balance()

fran.make_deposit(1000).make_withdrawal(100).make_withdrawal(200).make_withdrawal(300).display_user_balance()

# zach.transfer_money(fran, 500)
# zach.display_user_balance()
# fran.display_user_balance()

zach.transfer_money(fran, 500).display_user_balance()
fran.display_user_balance()