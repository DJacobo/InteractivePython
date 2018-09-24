# cd "C:\Users\Daniel\Documents\Python Scripts\InteractivePython"
# pytest test_IP_Ch1_17_Deck.py
# ===============================================================
import unittest
from IP_Ch1_17_Deck import Deck, Card

class deckTest(unittest.TestCase):
    def setUp(self):
        self.suitsDict = {'Clubs': 1, 'Spades': 2, 'Diamonds':3, 'Hearts':4}
        self.faceDict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        self.deck = Deck(self.suitsDict, self.faceDict)
        self.cardD2 = Card('Diamonds', 3, '2', 2)
        self.cardH2 = Card('Hearts', 4, '2', 2)
        self.cardHK = Card('Hearts', 4, 'K', 13)
        self.cardEqualHK = Card('Hearts', 4, 'K', 13)

    def test_Card_getSuit(self):
        self.assertEqual('Hearts', self.cardH2.getSuit())

    def test_Card_getSuit_False(self):
        self.assertNotEqual('Spades', self.cardH2.getSuit())

    def test_Card_getFaceValue(self):
        self.assertEqual(2, self.cardH2.getFaceValue())

    def test_Card_getValue_False(self):
        self.assertNotEqual(7, self.cardH2.getFaceValue())

    def test_Card_getColor(self):
        self.assertEqual('Red', self.cardH2.getColor())

    def test_Card_getColor_False(self):
        self.assertNotEqual('Black', self.cardH2.getColor())

    def test_Card_lessNum(self):
        self.assertTrue(self.cardH2 < self.cardHK)

    def test_Card_lessNum_False(self):
        self.assertFalse(self.cardHK < self.cardH2)

    def test_Card_lessSuit(self):
        self.assertTrue(self.cardD2.getSuitValue() < self.cardH2.getSuitValue())

    def test_Card_lessSuit_False(self):
        self.assertFalse(self.cardH2.getSuitValue() < self.cardD2.getSuitValue())

    def test_Card_lessEqualNum(self):
        self.assertTrue(self.cardH2 <= self.cardEqualHK)

    def test_Card_lessEqualNum_False(self):
        self.assertFalse(self.cardHK <= self.cardH2)

    def test_Card_greaterEqual(self):
        self.assertTrue(self.cardHK >= self.cardH2)

    def test_Card_greaterEqual_False(self):
        self.assertFalse(self.cardH2 >= self.cardEqualHK)

    def test_Card_greaterNum(self):
        self.assertTrue(self.cardHK > self.cardH2)

    def test_Card_greaterNum_False(self):
        self.assertFalse(self.cardH2 > self.cardHK)

    def test_Card_greaterSuit(self):
        self.assertTrue(self.cardH2.getSuitValue() > self.cardD2.getSuitValue())

    def test_Card_greaterSuit_False(self):
        self.assertFalse(self.cardD2.getSuitValue() > self.cardH2.getSuitValue())
