'''
Justin Young
Lab 10
Version1&2
'''
import time
from time import time, ctime
from time import mktime
t = time()

class ATM:
    transactions = ''
    def __init__(self, money):
        self.money = money    
    def check_balance(self):
        self.transactions += f'User checked balance of {self.money} @{ctime(t)}\n'
        return self.money
    def deposit(self, amount):
        self.money += amount
        self.transactions += f'User deposited {amount} @{ctime(t)}\n'
        return self.money
    def check_withdrawal(self, amount):
        if self.money < amount:
            self.transactions += f'User had insufficient funds to withdraw {amount} @{ctime(t)}\n'
            return False
        else:
            return True
    def withdraw(self, amount):
        self.money -= amount
        self.transactions += f'User withdrew {amount} @{ctime(t)}\n'
        return self.money
    def calc_interest(self):
        birth = (1983, 11, 23, 15, 58, 32, 2, 327, 0)
        b = mktime(birth)
        a = t - b
        years = (a / 86400) / 365
        c = self.money * 0.001 * years
        c = round(c, 2)
        self.transactions += f'Interest {c} calculated @{ctime(t)}\n'
        return c
        
    def print_transactions(self):
        return self.transactions




    




atm = ATM(150.00) # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        amount = float(input('How much would you like to deposit? '))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')
    elif command == 'withdraw':
        amount = float(input('How much would you like '))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'transactions':
        print(atm.print_transactions())
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('transactions - check prior user transactions')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')