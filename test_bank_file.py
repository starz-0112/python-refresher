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
        a_Bank = bank_file.Bank(500, "Mark", 1011235)
        self.assertEqual(a_Bank.balance, 500)
        self.assertNotEqual(a_Bank.balance, 780)