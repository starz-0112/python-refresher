class Bank(object):
    def __init__(self, balance, name, account_num):
        """ Upon initialization, create an account with set balance, name, and account_num. """
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance = balance
        else:
            return("Please put in an integer for your balance!")
        
        if isinstance(name, str):
            self.name = name
        else:
            return("Please put in a string for your name!")
        
        if isinstance(account_num, int) or isinstance(account_num, float):
            self.account_num = account_num
        else:
            return("Please put in an integer for your account number!")
    
    def withdraw(self, withdraw_amt):
        """ Will withdraw money from account, if parameter is int."""
        if isinstance(withdraw_amt, int) or isinstance(withdraw_amt, float):
            self.balance -= withdraw_amt
        else:
            return("Please put in an integer for your withdraw amount!")
        
    def deposit(self, deposit_amt):
        """ Will deposit money into account, if parameter is int. """
        if isinstance(deposit_amt, int) or isinstance(deposit_amt, float):
            self.balance += deposit_amt
        else:
            return("Please put in an integer for your deposit amount!")
        
    def print_current_balance(self):
        """ Print current balance. """
        print("The current balance is: " + str(self.balance))