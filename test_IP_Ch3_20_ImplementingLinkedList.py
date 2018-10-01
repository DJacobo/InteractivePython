from IP_Ch3_20_ImplementingLinkedList import *
import unittest

class TestMyLinkedList(unittest.TestCase):
    def setUp(self):
        self.mylist = MyUnorderedLinkedList()
        self.mylist.addData(31)
        self.mylist.addData(77)
        self.mylist.addData(17)
        self.mylist.addData(93)
        self.mylist.addData(26)
        self.mylist.addData(54)

    def test_myLinkedList_size(self):
        self.assertEqual(6, self.mylist.size())
    def test_myLinkedList_search(self):
        self.assertTrue(self.mylist.search(31))
    def test_myLinkedList_pop_0(self):
        self.assertEqual(31, self.mylist.pop(0))
    def test_myLinkedList_pop_end(self):
        self.assertEqual(54, self.mylist.pop())
    def test_myLinkedList_sizePopped(self):
        self.mylist.removeData(77)
        self.mylist.pop(0)
        self.mylist.pop()
        self.assertEqual(3, self.mylist.size())
    def test_myLinkedList_insert_index(self):
        self.mylist.insert(1, 1000)
        self.assertEqual(1, self.mylist.index(1000))
    def test_myLinkedList_append_pop(self):
        self.mylist.append(50)
        self.assertEqual(50, self.mylist.pop())
    def test_myLinkedList_sizeInserted(self):
        self.mylist.addData(1)
        self.mylist.insert(0, 2)
        self.mylist.append(50)
        self.assertEqual(9, self.mylist.size())

if __name__ == '__main__':
    __main__ = unittest.main()