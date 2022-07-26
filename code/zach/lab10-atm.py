from datetime import datetime

class ATM:

    def __init__(self, balance=0, interest_rate=0.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        """Returns the account balance."""
        self.transactions.append({'Date': datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"), 'transaction_type': 'checked balance', 'balance': self.balance})
        return self.balance

    def deposit(self, amount):
        """Deposits the given amount in the account."""
        previous_balance = self.balance
        self.balance += amount
        self.transactions.append({'Date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'transaction_type': 'deposit',
            'amount': amount, 'previous_balance': previous_balance, 'new_balance': self.balance})
        return self.balance

    def check_withdrawal(self, amount):
        """Returns true if the withdrawn amount won't put the account in the negative"""
        if self.balance - amount >= 0: 
            return True
        else:
            self.transactions.append({'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'transaction_type': 'Withdrawal', 'result': 'insufficient funds',
                'amount': amount, 'balance': self.balance})
            return False

    def withdraw(self, amount):
        """Withdraws the amount from the account and returns it."""
        previous_balance = self.balance
        self.balance -= amount
        self.transactions.append({'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'transaction_type': 'Withdrawal',
            'amount': amount, 'previous_balance': previous_balance, 'new_balance': self.balance})
        return self.balance

    def calc_interest(self):
        """Returns the amount of interest calculated on the account."""
        return self.balance * self.interest_rate


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount)  # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        # call the check_withdrawal(amount) method
        if atm.check_withdrawal(amount):
            atm.withdraw(amount)  # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        for transaction in atm.transactions:
            print(transaction)
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - print a list of transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')
