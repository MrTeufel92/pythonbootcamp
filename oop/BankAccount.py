

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit Accepted, added {amount} to your balance.')
        print(f'Current balance is: {self.balance}')

    def withdraw(self, amount):
        if self.balance < amount:
            print('Funds Unavailable!')
            print(f'Current balance is: {self.balance} and you tried to withdraw amount: {amount}')
        else:
            self.balance -= amount
            print(f'Withdrawal Accepted, withdrew {amount} from your balance.')
            print(f'Current balance is: {self.balance}')

    def __str__(self):
        return f'Account owner:   {self.owner}' + '\n' + f'Account balance: {self.balance}'


account = Account('Miki', 100)

print(account)

account.deposit(30)

account.withdraw(100)

account.withdraw(50)
