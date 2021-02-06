#%%
class Account():
    
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        '''
        An account class, has owner and balance attributes and allows balance withdrawal and deposition.
        '''
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float) -> None:
        '''
        Withdraw a provided amount from account balance if there is available balance to be withdrawn.
        '''
        if amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrawn {amount}.")
        else:
            print("Not enough balance.")

    def deposit(self, amount: float) -> None:
        '''
        Add an amount to the account balance.
        '''
        self.balance += amount
        print(f"Added {amount} to the account balance.")

    def __str__(self) -> str:
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

account = Account("Mano", 350.0)
print(account)
account.deposit(100.0)
print(account)
account.withdraw(430)
print(account)
account.withdraw(100.0)
print(account)
# %%
