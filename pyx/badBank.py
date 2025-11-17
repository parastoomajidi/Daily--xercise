#Encapsulation

class BadBankAccount:
    def __init__(self, balancz):
        self.balance = balancz


# account = BadBankAccount(0.0)
# account.balance = -1
# print(account.balance)

class BankAcount :
    def __init__(self):
        self._balance = 0.0 

# seeter props
    @property
    def balance(self):
        return self._balance
    
    def deposit (self, amount):
        if amount <= 0 :
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount


    # draw the method

    def withdraw (self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        if amount >= self._balance:
            raise ValueError ("Insufficient funds")
        self._balance -= amount



# create an account from bank account
account = BankAcount()
print(account.balance)
account.deposit(1.99)
print(account.balance)
account.withdraw(1)
print(account.balance)




