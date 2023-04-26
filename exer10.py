import unittest
from exer7 import BankAccount, StudentAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Test Test", "1000000", 1000)
        
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)
        
    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)
    
class TestStudentAccount(unittest.TestCase):
    
    def setUp(self):
        self.account = StudentAccount("Stud Stud", "2000000", 1000)
        
    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)
        
    def test_withdraw(self):
        self.account.withdraw(500)
        self.assertEqual(self.account.balance, 500)
        
if __name__ == '__main__':
    unittest.main()