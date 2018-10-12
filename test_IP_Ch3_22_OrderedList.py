from IP_Ch3_22_OrderedList import *
import unittest

class TestMyOrderedList(unittest.TestCase):
    def setUp(self):
        self.mylist = MyOrderedList()
        self.mylist.add(31)
        self.mylist.add(77)
        self.mylist.add(17)
        self.mylist.add(93)
        self.mylist.add(26)
        self.mylist.add(54)

    def test_myOrderedList_size(self):
        self.assertEqual(6, self.mylist.size())
    def test_myOrderedList_search(self):
        self.assertTrue(self.mylist.search(31))
    def test_myOrderedList_search_False(self):
        self.assertFalse(self.mylist.search(32))
    def test_myOrderedList_index(self):
        self.assertEqual(2, self.mylist.index(31))
    def test_myOrderedList_index_False(self):
        self.assertEqual(-1, self.mylist.index(1000))
    def test_myOrderedList_pop_0(self):
        self.assertEqual(17, self.mylist.pop(0))
    def test_myOrderedList_pop_end(self):
        self.assertEqual(93, self.mylist.pop())
    def test_myOrderedList_addIndex(self):
        self.mylist.add(1000)
        self.assertEqual(6, self.mylist.index(1000))
    def test_myOrderedList_sizePopped(self):
        self.mylist.remove(77)
        self.mylist.pop(0)
        self.mylist.pop()
        self.assertEqual(3, self.mylist.size())
    def test_myOrderedList_sizeInserted(self):
        self.mylist.add(1)
        self.mylist.add(2)
        self.mylist.add(50)
        self.assertEqual(9, self.mylist.size())

if __name__ == '__main__':
    __main__ = unittest.main()