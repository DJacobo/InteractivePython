from IP_Ch5_12_QuickSort import *
import unittest

class TestQuickSort(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [1]
        self.ascending = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.descending = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.shuffled = [8, 4, 6, 9, 1, 2, 3, 7, 5]
        self.exList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.exSort = [17, 20, 26, 31, 44, 54, 55, 77, 93]
        self.dupeList = [9, 8, 7, 6, 5, 5, 4, 3, 2, 1]
        self.dupeSort = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]

    def test_quickSort_empty(self):
        self.assertEqual([], quickSort(self.empty))
    def test_quickSort_single(self):
        self.assertEqual(self.single, quickSort(self.single))
    def test_quickSort_ascending(self):
        self.assertEqual(self.ascending, quickSort(self.ascending))
    def test_quickSort_descending(self):
        self.assertEqual(self.ascending, quickSort(self.descending))
    def test_quickSort_shuffle(self):
        self.assertEqual(self.ascending, quickSort(self.shuffled))
    def test_quickSort_duplicate(self):
        self.assertEqual(self.dupeSort, quickSort(self.dupeList))
    def test_quickSort_example(self):
        self.assertEqual(self.exSort, quickSort(self.exList))

if __name__ == '__main__':
    __main__ = unittest.main()