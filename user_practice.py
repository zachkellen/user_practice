class User:
    # declaring a class atrribute
    bank_name = "First National Dojo"
    # Initialize with two parameters
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

        # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


zach = User('Zach Kellen', 'zach@codingdojo.com')
kylee = User('Kylee F', 'kyleef@codingdojo.com')
fran = User('Fran M', 'franm@codingdojo.com')

zach.make_deposit(50)
zach.make_deposit(100)
zach.make_deposit(200)
zach.make_withdrawal(150)
zach.display_user_balance()

kylee.make_deposit(200)
kylee.make_deposit(300)
kylee.make_withdrawal(100)
kylee.make_withdrawal(200)
kylee.display_user_balance()

fran.make_deposit(1000)
fran.make_withdrawal(100)
fran.make_withdrawal(200)
fran.make_withdrawal(300)
fran.display_user_balance()

zach.transfer_money(fran, 500)
zach.display_user_balance()
fran.display_user_balance()