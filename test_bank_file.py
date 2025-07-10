# from bank_file import Bank

# a_Bank = Bank(400, "Bethany", 783)
# a_Bank.withdraw(590)
# a_Bank.withdraw(90)
# a_Bank.deposit(500)
# a_Bank.withdraw(-90)
# a_Bank.deposit(-500)
# a_Bank.print_current_balance()

import unittest
import bank_file


class TestBank(unittest.TestCase):
    def test_bank_setup(self):
        """Hard test the init method to make sure everything is set up correctly."""
        a_Bank = bank_file.Bank(500, "Nemo", 1011235)
        self.assertEqual(a_Bank.balance, 500)       #check bank balane
        self.assertNotEqual(a_Bank.balance, 780)
        self.assertEqual(a_Bank.name, "Nemo")       #check bank name
        self.assertEqual(a_Bank.account_num, 1011235)       #check bank account num
        self.assertNotEqual(a_Bank.account_num, 4)
        self.assertNotEqual(type(a_Bank.account_num), str)      #check type of bank account num
    def test_bank_withdraw(self):
        """Hard test the withdrawing feature of the class. Make sure it's not modifying any other number. Make sure it does not let users withdraw too much or withdraw negative money."""
        a_Bank = bank_file.Bank(500, "Nemo", 1011235)
        self.assertEqual(a_Bank.balance, 500)       #check pre-balance
        self.assertNotEqual(a_Bank.balance, 780)
        a_Bank.withdraw(100)
        self.assertEqual(a_Bank.balance, 400)       #check post-balance
        self.assertNotEqual(a_Bank.balance, 200)
        self.assertNotEqual(a_Bank.account_num, 100)        #check account num - should be unmodified
        self.assertEqual(a_Bank.account_num, 1011235)
        self.assertEqual(a_Bank.withdraw(900), False)       #check withdrawing too much is not allowed
        self.assertEqual(a_Bank.withdraw(-80), False)       #check withdrawing negative is not allowed
        self.assertNotEqual(a_Bank.withdraw(0), False)        #withdrawing 0 should be allowed
    def test_bank_deposit(self):
        """Hard test the deposit feature of the class. Make sure it does not accept negatives."""
        a_Bank = bank_file.Bank(500, "Nemo", 1011235)
        self.assertEqual(a_Bank.balance, 500)       #check pre-balance
        self.assertNotEqual(a_Bank.balance, 20)
        a_Bank.deposit(90)
        self.assertEqual(a_Bank.balance, 590)       #check post-balance
        self.assertNotEqual(a_Bank.balance, 410)
        self.assertNotEqual(a_Bank.account_num, 100)        #check account num - should be unmodified
        self.assertEqual(a_Bank.account_num, 1011235)
        self.assertEqual(a_Bank.deposit(-5), False)        #check depositing negative is not allowed
        self.assertEqual(a_Bank.deposit(-1), False)
        self.assertNotEqual(a_Bank.deposit(0), False)       #depositing 0 should be allowed
    def test_bank_printing(self):
        """Hard test the printing balance statement part."""
        a_Bank = bank_file.Bank(500, "Nemo", 1011235)
        self.assertEqual(a_Bank.balance, 500)       #check pre-balance, make sure it's still the right account
        self.assertNotEqual(a_Bank.balance, 20)
        self.assertEqual(type(a_Bank.print_current_balance()), int)     #check correct typing is printed and goes through
        self.assertNotEqual(type(a_Bank.print_current_balance()), str)      #remember, you put return balance value, not the printed str
        self.assertNotEqual(a_Bank.print_current_balance(), False)