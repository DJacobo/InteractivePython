import unittest
from IP_Ch3_9_PostFix import infixToPostfix

class TestPostFix(unittest.TestCase):
    def setUp(self):
        self.exp1 = 'A + B * C'
        self.res1 = 'A B C * +'
        self.exp2 = '( A + B ) * ( C + D )'
        self.res2 = 'A B + C D + *'
        self.exp3 = '( A + B ) * C'
        self.res3 = 'A B + C *'

    def test_infixToPostfix1(self):
        self.assertEqual(self.res1, infixToPostfix(self.exp1))
    def test_infixToPostfix2(self):
        self.assertEqual(self.res2, infixToPostfix(self.exp2))
    def test_infixToPostfix3(self):
        self.assertEqual(self.res3, infixToPostfix(self.exp3))

if __name__ == '__main__':
    unittest.main()