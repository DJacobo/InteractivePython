import unittest
from IP_CH3_6_BalanceParantheses import balanceString

class BalanceStringTest(unittest.TestCase):
    def setUp(self):
        self.b1 = '(()()()())'
        self.b2 = '(((())))'
        self.b3 = '(()((())()))'
        self.b4 = '{ {([][])}()}'
        self.b5 = '[[{{(())}}]]'
        self.b6 = '[][][](){}'

        self.n1 = '((((((())'
        self.n2 = '()))'
        self.n3 = '(()()(()'
        self.n4 = '([)]'
        self.n5 = '((()]))'
        self.n6 = '[{()]'

    def test_balanceString1(self):
        self.assertTrue(balanceString(self.b1))
    def test_balanceString2(self):
        self.assertTrue(balanceString(self.b2))
    def test_balanceString3(self):
        self.assertTrue(balanceString(self.b3))
    def test_balanceString4(self):
        self.assertTrue(balanceString(self.b4))
    def test_balanceString5(self):
        self.assertTrue(balanceString(self.b5))
    def test_balanceString6(self):
        self.assertTrue(balanceString(self.b6))

    def test_balanceString1_False(self):
        self.assertFalse(balanceString(self.n1))
    def test_balanceString2_False(self):
        self.assertFalse(balanceString(self.n2))
    def test_balanceString3_False(self):
        self.assertFalse(balanceString(self.n3))
    def test_balanceString4_False(self):
        self.assertFalse(balanceString(self.n4))
    def test_balanceString5_False(self):
        self.assertFalse(balanceString(self.n5))
    def test_balanceString6_False(self):
        self.assertFalse(balanceString(self.n6))

if __name__ == '__main__':
    unittest.main()