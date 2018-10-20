import unittest
from IP_Ch5_3_SequentialSearch import *

class TestSequentialSearch(unittest.TestCase):
    def setUp(self):
        self.tenList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.evenList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    
    def test_unorderedSequentialSearch(self):
        self.assertTrue(unorderedSequentialSearch(self.tenList, 4))
    def test_unorderedSequentialSearch_false(self):
        self.assertFalse(unorderedSequentialSearch(self.tenList, 10))
    def test_orderedSequentialSearch(self):
        self.assertTrue(unorderedSequentialSearch(self.evenList, 4))
    def test_orderedSequentialSearch_false(self):
        self.assertFalse(unorderedSequentialSearch(self.evenList, 9))

if __name__ == '__main__':
    __main = unittest.main()