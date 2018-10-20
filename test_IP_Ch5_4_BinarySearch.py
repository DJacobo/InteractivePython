import unittest
from IP_Ch5_4_BinarySearch import BinarySearch

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.tenList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.evenList = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    
    def test_binarySearch(self):
        self.assertTrue(BinarySearch(self.tenList, 4))
    def test_binarySearch_zero(self):
        self.assertTrue(BinarySearch(self.tenList, 0))
    def test_binarySearch_end(self):
        self.assertTrue(BinarySearch(self.tenList, 9))
    def test_binarySearch_false(self):
        self.assertFalse(BinarySearch(self.tenList, 11))
    def test_binarySearch_even(self):
        self.assertTrue(BinarySearch(self.evenList, 4))
    def test_binarySearch_even_false(self):
        self.assertFalse(BinarySearch(self.tenList, 11))

if __name__ == '__main__':
    __main__ = unittest.main()