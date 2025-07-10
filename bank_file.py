class Bank(object):
    def __init__(self, balance, name, account_num):
        """ Upon initialization, create an account with set balance, name, and account_num. """
        # Type checks
        if isinstance(balance, int) or isinstance(balance, float):
            self.balance = balance
        else:
            print("Please put in an integer for your balance!")
            return False
        
        if isinstance(name, str):
            self.name = name
        else:
            print("Please put in a string for your name!")
            return False
        
        if isinstance(account_num, int) or isinstance(account_num, float):
            self.account_num = account_num
        else:
            print("Please put in an integer for your account number!")
            return False

        # Greeting message
        print("Hey " + str(self.name) + ", welcome to your account, account #" + str(self.account_num) + ". Your current balance is: " + str(self.balance))
    
    def withdraw(self, withdraw_amt):
        """ Will withdraw money from account, if parameter is int."""
        # First check: is this amt withdrawable?
        if isinstance(withdraw_amt, int) or isinstance(withdraw_amt, float):
            # Second check: is this amt affordable?
            if withdraw_amt > self.balance or withdraw_amt < 0:
                print("Sorry! You cannot withdraw " + str(withdraw_amt) + " dollars.")
                return False
            else:
                self.balance -= withdraw_amt
                print("Thanks for withdrawing! Your new balance is " + str(self.balance))
                return True
        else:
            print("Please put in an integer for your withdraw amount!")
            return False
        
    def deposit(self, deposit_amt):
        """ Will deposit money into account, if parameter is int. """
        # Check: is amt depositable?
        if isinstance(deposit_amt, int) or isinstance(deposit_amt, float):
            if deposit_amt < 0:
                print("Sorry! You cannot deposit " + str(deposit_amt) + " dollars.")
                return False
            else:
                self.balance += deposit_amt
                print("Thanks for depositing! Your new balance is " + str(self.balance))
                return True
        else:
            print("Please put in an integer for your deposit amount!")
            return False
        
    def print_current_balance(self):
        """ Print current balance. """
        print("Your current balance is: " + str(self.balance))
        return self.balance

#raise(ValueError, "you broke") --> to raise error