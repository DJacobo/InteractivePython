from IP_Ch5_11_MergeSort import *
import unittest

class testMergeSort(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [1]
        self.ascending = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.descending = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.shuffled = [8, 4, 6, 9, 1, 2, 3, 7, 5]
        self.exList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
        self.exSort = [17, 20, 26, 31, 44, 54, 55, 77, 93]

    def test_mergeSort_empty(self):
        self.assertEqual([], mergeSort(self.empty))
    def test_mergeSort_single(self):
        self.assertEqual(self.single, mergeSort(self.single))
    def test_mergeSort_ascending(self):
        self.assertEqual(self.ascending, mergeSort(self.ascending))
    def test_mergeSort_descending(self):
        self.assertEqual(self.ascending, mergeSort(self.descending))
    def test_mergeSort_shuffle(self):
        self.assertEqual(self.ascending, mergeSort(self.shuffled))
    def test_mergeSort_example(self):
        self.assertEqual(self.exSort, mergeSort(self.exList))

if __name__ == '__main__':
    __main__ = unittest.main()