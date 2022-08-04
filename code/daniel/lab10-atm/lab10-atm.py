#=====================================================
#Version1
#=====================================================


# class ATM:

#     def __init__(self, balance=0, interest_rate=.001):
#         self.balance = balance
#         self.interest_rate = interest_rate
     
#     def check_balance(self):
#         return self.balance

#     def deposit(self, amount):
#         self.balance += amount
    
#     def check_withdraw(self, amount):
#         if self.balance - amount >= 0:
#             return True
#         else:
#             return False

#     def withdraw(self, amount): 
#         self.balance -= amount
    
#     def calc_interest(self):
#        return self.balance * self.interest_rate


# #=======================


# atm = ATM() # create an instance of our class
# print('Welcome to the ATM')
# while True:
#     command = input('Enter a command: ')
#     if command == 'balance':
#         balance = atm.check_balance() # call the check_balance() method
#         print(f'Your balance is ${balance}')
#     elif command == 'deposit':
#         amount = float(input('How much would you like to deposit? '))
#         atm.deposit(amount) # call the deposit(amount) method
#         print(f'Deposited ${amount}')
#     elif command == 'withdraw':
#         amount = float(input('How much would you like? '))
#         if atm.check_withdraw(amount): # call the check_withdrawal(amount) method
#             atm.withdraw(amount) # call the withdraw(amount) method
#             print(f'Withdrew ${amount}')
#         else:
#             print('Insufficient funds')
#     elif command == 'interest':
#         amount = atm.calc_interest() # call the calc_interest() method
#         atm.deposit(amount)
#         print(f'Accumulated ${amount} in interest')
#     elif command == 'help':
#         print('Available commands:')
#         print('balance  - get the current balance')
#         print('deposit  - deposit money')
#         print('withdraw - withdraw money')
#         print('interest - accumulate interest')
#         print('exit     - exit the program')
#     elif command == 'exit':
#         break
#     else:
#         print('Command not recognized')


#=====================================================
#Version2
#=====================================================


class ATM:

    def __init__(self, balance=0, interest_rate=.001):
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = []

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'User deposited ${amount}')

    def check_withdraw(self, amount):
        if self.balance - amount >= 0:
            return True
        else:
            return False

    def withdraw(self, amount): 
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount}')

    def calc_interest(self):
       return self.balance * self.interest_rate

    def print_transactions():
        return self.transactions


#=======================


atm = ATM() # create an instance of our class
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
        amount = float(input('How much would you like? '))
        if atm.check_withdraw(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')
    elif command == 'transactions':
        for transaction in atm.transactions:
            print(f'${transaction}')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')













