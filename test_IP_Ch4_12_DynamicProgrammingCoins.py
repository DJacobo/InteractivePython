import unittest
from IP_Ch4_12_DynamicProgrammingCoins import *

class TestMinCoinsDynamic(unittest.TestCase):
    def setUp(self):
        self.usCoinList = [1, 5, 10, 25]
        self.EboniaCoinList = [1, 5, 10, 21, 25]
        self.fiftyCoinList = [1, 5, 10, 25, 50]

    def test_minCoinsDynamic_us(self):
        self.assertEqual(3, minCoinsDynamic(75, self.usCoinList))
    def test_minCoinsDynamic_fifty(self):
        self.assertEqual(2, minCoinsDynamic(75, self.fiftyCoinList))
    def test_minCoinsDynamic_ebonia(self):
        self.assertEqual(3, minCoinsDynamic(63, self.EboniaCoinList))

if __name__ == '__main__':
    __main__ = unittest.main()