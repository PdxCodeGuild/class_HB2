# lab10 - ATM v1

class ATM:
    
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        # balance = 0
        interest_rate = 0.001 

    # returns the account balance
    def check_balance(self):
        return self.balance
    
    # deposits the given amount in the account
    def deposit(self, amount):
        self.balance += amount   
    
    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        if self.balance < amount:
            return False
        else:
            return True
        
    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        self.balance -= amount
        
    # returns the amount of interest calculated on the account
    def calc_interest(self):
        p = self.balance
        t = float(input("Enter the number of years : "))
        r = self.interest_rate
        return p * (pow((1 + r / 100), t))

atm = ATM(0, 0.001) # create an instance of our class
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
    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount:.2f} in interest')
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



