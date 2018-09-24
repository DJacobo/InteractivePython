import unittest
from IP_Ch3_8_DecimalToBinary import decimalToBinary, baseToBinary

class TestDecimalToBinary(unittest.TestCase):
    def setUp(self):
        self.testZero = 0
        self.testTen = 10
        self.testEven = 42
        self.testOdd = 155

        self.baseBin = 2
        self.baseOct = 8
        self.baseDec = 10
        self.baseHex = 16

    def test_DecimalToBinary_Zero(self):
        self.assertEqual('0', decimalToBinary(self.testZero))
    def test_DecimalToBinary_Ten(self):
        self.assertEqual('1010', decimalToBinary(self.testTen))
    def test_DecimalToBinary_Even(self):
        self.assertEqual('101010', decimalToBinary(self.testEven))
    def test_DecimalToBinary_Odd(self):
        self.assertEqual('10011011', decimalToBinary(self.testOdd))

    def test_BaseToBinary_BinZero(self):
        self.assertEqual('0', baseToBinary(self.baseBin, self.testZero))
    def test_BaseToBinary_BinTen(self):
        self.assertEqual('1010', baseToBinary(self.baseBin, self.testTen))
    def test_BaseToBinary_BinEven(self):
        self.assertEqual('101010', baseToBinary(self.baseBin, self.testEven))
    def test_BaseToBinary_BinOdd(self):
        self.assertEqual('10011011', baseToBinary(self.baseBin, self.testOdd))

    def test_BaseToBinary_OctZero(self):
        self.assertEqual('0', baseToBinary(self.baseOct, self.testZero))
    def test_BaseToBinary_OctTen(self):
        self.assertEqual('12', baseToBinary(self.baseOct, self.testTen))
    def test_BaseToBinary_OctEven(self):
        self.assertEqual('52', baseToBinary(self.baseOct, self.testEven))
    def test_BaseToBinary_OctOdd(self):
        self.assertEqual('233', baseToBinary(self.baseOct, self.testOdd))

    def test_BaseToBinary_HexZero(self):
        self.assertEqual('0', baseToBinary(self.baseHex, self.testZero))
    def test_BaseToBinary_HexTen(self):
        self.assertEqual('A', baseToBinary(self.baseHex, self.testTen))
    def test_BaseToBinary_HexEven(self):
        self.assertEqual('2A', baseToBinary(self.baseHex, self.testEven))
    def test_BaseToBinary_HexOdd(self):
        self.assertEqual('9B', baseToBinary(self.baseHex, self.testOdd))

if __name__ == '__main__':
    unittest.main()