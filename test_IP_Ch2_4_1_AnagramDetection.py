# cd "C:\Users\Daniel\Documents\Python Scripts\InteractivePython"
# pytest test_IP_Ch2_4_1_AnagramDetection.py
# ===============================================================
import unittest
from IP_Ch2_4_1_AnagramDetection import *

class AnagramDetectionTest(unittest.TestCase):
    def setUp(self):
        self.ana = 'Anagram'
        self.gram = 'mAnagra'
        self.wrongSize = 'notAnAnagram'
        self.wrongLetters = 'Bananas'

    def test_AnagramCheckOff(self):
        self.assertTrue(anagramCheckOff(self.ana, self.gram))

    def test_AnagramCheckOff_False(self):
        self.assertFalse(anagramCheckOff(self.ana, self.wrongSize))

    def test_AnagramCheckOff_Letters_False(self):
        self.assertFalse(anagramCheckOff(self.ana, self.wrongLetters))
        
    def test_AnagramSortCompare(self):
        self.assertTrue(anagramSortCompare(self.ana, self.gram))
        
    def test_AnagramSortCompare_False(self):
        self.assertFalse(anagramSortCompare(self.ana, self.wrongSize))

    def test_AnagramSortCompare_Letters_False(self):
        self.assertFalse(anagramSortCompare(self.ana, self.wrongLetters))

    def test_AnagramCountCompare(self):
        self.assertTrue(anagramCountCompare(self.ana, self.gram))
        
    def test_AnagramCountCompare_False(self):
        self.assertFalse(anagramCountCompare(self.ana, self.wrongSize))

    def test_AnagramCountCompare_Letters_False(self):
        self.assertFalse(anagramCountCompare(self.ana, self.wrongLetters))