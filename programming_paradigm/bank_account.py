class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f'Your {amount} added, New balance is: {self.balance}')
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'Your {amount} withdraw, New balance is: {self.balance}')
        else:
            print('Your balance isn\'t enough')
            
    def current_balnce(self):
        print(f'Your balance is: {self.balance}')
