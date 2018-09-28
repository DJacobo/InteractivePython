import unittest
from IP_Ch4_5_RecursiveFunctions import *

class test_RecursiveString(unittest.TestCase):
    def setUp(self):
        self.reverse = 'reverse'
        self.empty = ''
        self.palA = 'aibohphobia'
        self.palAlaska = 'Kanakanak' # a town in Alaska
        self.palElba = 'Able was I ere I saw Elba'
        self.palG = 'Go hang a salami; I’m a lasagna hog'
        self.palK = 'kayak'
        self.palL = 'Live not on evil'
        self.palM = 'madam i’m adam'
        self.palR = 'Reviled did I live, said I, as evil I did deliver'
        self.palSD = 'Wassamassaw' # a town in South Dakota
        self.notPal = 'Not a palindrome'

    def test_numToBaseString_bin(self):
        self.assertEqual('1', numToBaseString(1, 2))
    def test_numToBaseString_dec(self):
        self.assertEqual('16', numToBaseString(16, 10))
    def test_numToBaseString_hex(self):
        self.assertEqual('A', numToBaseString(10, 16))

    def test_recursiveReverseString(self):
        self.assertEqual('esrever', recursiveReverseString('reverse'))
    def test_recursiveReverseString_False(self):
        self.assertNotEqual('fake', recursiveReverseString('reverse'))
    def test_recursiveReverseString_empty(self):
        self.assertEqual('', recursiveReverseString(''))

    def test_palindromeDetector_empty(self):
        self.assertTrue(palindromeDetector(self.empty))
    def test_palindromeDetector_palA(self):
        self.assertTrue(palindromeDetector(self.palA))
    def test_palindromeDetector_palAlaska(self):
        self.assertTrue(palindromeDetector(self.palAlaska))
    def test_palindromeDetector_palElba(self):
        self.assertTrue(palindromeDetector(self.palElba))
    def test_palindromeDetector_palG(self):
        self.assertTrue(palindromeDetector(self.palG))
    def test_palindromeDetector_palK(self):
        self.assertTrue(palindromeDetector(self.palK))
    def test_palindromeDetector_palL(self):
        self.assertTrue(palindromeDetector(self.palL))
    def test_palindromeDetector_palM(self):
        self.assertTrue(palindromeDetector(self.palM))
    def test_palindromeDetector_palR(self):
        self.assertTrue(palindromeDetector(self.palR))
    def test_palindromeDetector_palSD(self):
        self.assertTrue(palindromeDetector(self.palSD))
    def test_palindromeDetector_false(self):
        self.assertFalse(palindromeDetector(self.notPal))

if __name__ == '__main__':
    __main__ = unittest.main()
    