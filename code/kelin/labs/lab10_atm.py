# Kelin Ray

# # Lab 10: ATM


class ATM: # Let's represent an ATM with a class containing two attributes: a balance and an interest rate.
    
    def __init__(self, balance, interest_rate): # Implement the initializer, as well as the following functions:
        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = [] # Created list of transactions for version 2
        # balance = 0
        interest_rate = 0.001 # Interest rate

        # - `check_balance()` returns the account balance
        # - `deposit(amount)` deposits the given amount in the account
        # - `check_withdrawal(amount)` returns true if the withdrawn amount won't put the account in the negative
        # - `withdraw(amount)` withdraws the amount from the account and returns it
        # - `calc_interest()` returns the amount of interest calculated on the account

    def check_balance(self): # Gets account balance
        return self.balance
    
    def deposit(self, amount): # Deposits to the balance
        self.balance += amount
        self.transactions.append(f'Deposit for ${amount}') # Adds deposit to transactions
    
    def check_withdrawal(self, amount): # Checks that amount is available
        if self.balance < amount:
            return False
        else:
            return True
        
    def withdraw(self, amount): # Makes the withdrawl from the balance
        self.balance -= amount
        self.transactions.append(f'Withdrawl for ${amount}')  # Adds withdraw to transactions
        
    def calc_interest(self): # A newly created account will default to a balance of 0 and an interest rate of 0.1%.
        p = self.balance
        t = float(input("Enter the number of years: "))
        r = self.interest_rate
        return p * (pow((1 + r / 100), t))

## Version 2

# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. 
# Add a new method `print_transactions()` to your class for printing out the list of transactions, and add a `transactions` option to your REPL loop.

    def print_transactions(self):
        for i in self.transactions:
            print(i)
        if self.transactions == []:
            print('No transactions') # If no transactions

# REPL loop

atm = ATM(0, 0.001) # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command or type help: ')
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
        print(f'Accumulated ${amount} in interest')

    elif command == 'transactions': # Version 2 added transactions
        atm.print_transactions()

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - get transactions') # Added transactions for version 2
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')