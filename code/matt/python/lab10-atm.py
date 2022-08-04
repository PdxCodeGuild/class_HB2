class ATM:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
        self.transactions = []

    def check_balance (self):
            return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}. New balance is {self.balance}")
    

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        if self.balance < amount:
            return False
    
    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}. New balance is {self.balance}")

    def calc_interest(self):
        try: 
            t = float(input("Enter the number of years in intergers: "))
            r = self.interest
            p = self.balance
            result = f'Your interest is: ${t * r * p}\nYour balance after interest is: ${p - (p * r * t)}'
            return result  
        except:
            return "We were unable to process that input\nMake sure you only input integers"

    
lines_for_looks = "--------------------"
print('Welcome to the ATM')

atm = ATM(0, 0.005)
while True:

    command = input('Enter a command: ')

    if command == 'balance':
        balance = atm.check_balance()
        print(lines_for_looks)
        print(f'Your balance is ${balance}')

    elif command == 'deposit':
        try:
            amount = float(input('How much would you like to deposit? '))
            atm.deposit(amount)
            print(lines_for_looks)
            print(f'Deposited ${amount}')
        except:
            print(lines_for_looks)
            print("We were unable to process that input\nMake sure you only input integers")

    elif command == 'withdraw':
        try:
            amount = float(input('How much would you like '))
            if atm.check_withdrawal(amount): 
                atm.withdraw(amount)
                print(lines_for_looks)
                print(f'Withdrew ${amount}')
            else:
                print(lines_for_looks)
                print('Insufficient funds')
        except: 
            print(lines_for_looks)
            print("We were unable to process that input\nMake sure you only input integers")

    elif command == 'interest':
        print(lines_for_looks)
        print(atm.calc_interest())
    
    elif command == 'transactions':
        print(lines_for_looks)
        print(f'TRANSACTIONS - {atm.transactions}')

    elif command == 'help':
        print(lines_for_looks)
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')
        print('transactions - view recent transactions')

    elif command == 'exit':
        break

    else:
        print(lines_for_looks)
        print('Command not recognized')


