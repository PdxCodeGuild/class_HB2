
# class Drink:
#     def __init__(self, owner, cup_volume):
#         self.volume = 0
#         self.cup_volume = cup_volume
#         self.owner = owner



    # def sip_drink(self, size):
    #     # lower drink's volume by some small amount
    #     if size == 'gulp':
    #         self.volume -= 2.5
    #     elif size == 'chug':
    #         self.volume -= self.volume
    #     else:
    #         self.volume -= .1
    #     return self.volume

#================================================




class ATM:
    def __init__(self, balance = 0, interest = .001):
        self.balance = balance
        self.interest = interest
        self.transactions = []

    def check_balance(self):
        # returns the account balance
        return self.balance

    def deposit(self, amount):
        #  deposits the given amount in the account
        self.balance += amount
        deposit_str = f"user deposited ${amount}"
        self.transactions.append(deposit_str)
        return self.balance
        
        
    def check_withdraw(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        if self.balance < amount:
            return False
        else:
            return True
    def withdraw(self, amount):
        # withdraws the amount from the account and returns it
        self.balance -= amount


    def calc_interest(self):
        # returns the amount of interest calculated on the account
        interest = self.balance * .001
        return round(interest, 2)
        


#=========================================================
    def print_transactions(self):
        if




#================================================
atm = ATM() # create an instance of our class
print('Welcome to the ATM')
while True:
    command = input('Enter a command: ')
    if command == 'balance':
        balance = atm.check_balance() # call the check_balance() method
        print(f'Your balance is ${balance}')
    elif command == 'deposit':
        deposit = float(input('How much would you like to deposit? '))
        atm.deposit(deposit) # call the deposit(amount) method
        print(f'Deposited ${deposit}')
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
    # elif command == 'help':
    #     print('Available commands:')
    #     print('balance  - get the current balance')
    #     print('deposit  - deposit money')
    #     print('withdraw - withdraw money')
    #     print('interest - accumulate interest')
    #     print('exit     - exit the program')
    # elif command == 'exit':
    #     break
    # else:
    #     print('Command not recognized')