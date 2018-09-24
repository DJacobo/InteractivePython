# cd "C:\Users\Daniel\Documents\Python Scripts\InteractivePython"
# pytest test_CrackingTheInterview_1_1.py
import unittest
from CrackingTheInterview_Ch1 import isUnique
class test_Cracking(unittest.TestCase):
    def setUp(self):
        self.abc = 'abcdefghijklmnopqrstuvwxyz'
        self.baby = 'baby'
        self.empty = ''
        self.spaces = 'abc def ghi'

    def test_isUnique_abc(self):
        self.assertTrue(isUnique(self.abc))

    def test_isUnique_baby(self):
        self.assertFalse(isUnique(self.baby))

    def test_isUnique_empty(self):
        self.assertTrue(isUnique(self.empty))

    def test_isUnique_spaces(self):
        self.assertFalse(isUnique(self.spaces))

if __name__ == '__main__':
    unittest.main()