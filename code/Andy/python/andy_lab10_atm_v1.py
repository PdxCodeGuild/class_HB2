class ATM:
    def __init__(self, balance_arg = 0, intrest_rate_arg = .001): #positional arguments. a method. a more flexable way to do it 
        self.balance = balance_arg  #balance_arg are local varable 
        self.intrest_rate = intrest_rate_arg 
        self.transactions = []
        
    
    # def __init__(self): #positional arguments. a method
    #     self.balance = 0 one way to do it 
    #     self.intrest_rate = .001 

    def check_balance(self): # going into self to retrieve balance from what you have 
        return self.balance  #Returning is used to return a value from a function and exit the function. To return a value from a function, use the return keyword. and print means display a value dont think it'll exit the function 
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'user deposited {amount}')
        return self.balance
    
    def check_withdrawal(self, amount): #using self to get balance and amount since thats what we're checking 
        if self.balance >= amount:
            return True
        else:
            return False
        
    def withdraw(self, amount):
        self.balance -= amount 
        self.transactions.append(f'user withdrew {amount}') 
        return self.balance

    def calc_interest(self):
        interest = self.balance * self.intrest_rate * .01
        return interest
    
    def print_transactions(self):
        for i in self.transactions:
            print(i)
            return self.transactions


# atm = ATM(5, .001) #putting the values for the initializer.its an object
# # print("atm bal: ", atm.balance) #just for testing but not done in real life
# # print('atm rate: ', atm.intrest_rate)#just for testing but not done in real life

# atm.check_balance() #atm is object and checkbalance is the method access the balance
# # print('calling check_balance method: ', atm.check_balance())
# the_balance = atm.check_balance()



atm = ATM() # create an instance of our class case sensative make the same as the class being called
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
        print(f'Accumulated ${amount} in interest')
    elif command == "transactions":
         transactions = atm.print_transactions()
         print(f'your transaction history is {transactions}')
    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('transactions - view transactions')
        print('exit     - exit the program')
    elif command == 'exit':
        break
    else:
        print('Command not recognized')