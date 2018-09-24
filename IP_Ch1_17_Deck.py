# Deck HAS-A (52) Card(s)
#   No duplicates (Other than jokers if necessary)
# Card
#   Suit, Num

class Deck:
    def __init__(self, suitsDict=None, faceDict=None):
        # suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
        # values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        if suitsDict == None:
            # Default uses poker rules, suit has no rank in poker, Ace is highest
            suitsDict = {'Clubs': 1, 'Spades': 1, 'Diamonds':1, 'Hearts':1}
        if faceDict == None:
            faceDict = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13, 'A':14}
        self.cards = []
        for suit in suitsDict:
            for face in faceDict:
                self.cards.append(Card(suit, suitsDict[suit], face, faceDict[face]))

    def drawCard(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            raise IndexError('There are no more cards in the deck')

    def viewDeck(self):
        print('%s cards remaining!' % len(self.cards))
        for card in self.cards:
            print(card)

    # TODO: Various rules for decks, Shuffle, multipleDraw

class Card:
    def __init__(self, s, sv, f, fv):
        self.suit = s
        self.suitValue = sv
        self.face = f
        self.faceValue = fv

    def getSuit(self):
        return self.suit

    def getSuitValue(self):
        return self.suitValue

    def getFace(self):
        return self.face

    def getFaceValue(self):
        return self.faceValue

    def getColor(self):
        s = self.getSuit()
        if s == 'Clubs' or s == 'Spades':
            return 'Black'
        else:
            return 'Red'

    def __str__(self):
        return '%s of %s' % (self.getFace(), self.getSuit())

    def __repr__(self):
        return 'Card(%r,, %r, %r %r)' % (self.getSuit(), self.getSuitValue(), self.getFace(), self.getFaceValue())

    # TODO: lt, le, gt, ge, eq, ne
    def __eq__(self, otherCard):
        if self.getFaceValue() == otherCard.getFaceValue() and self.getSuitValue() == otherCard.getSuitValue():
            return True
        else:
            return False

    def __lt__(self, otherCard):
        if self.getFaceValue() < otherCard.getFaceValue():
            return True
        elif self.getFaceValue() == otherCard.getFaceValue():
            if self.getSuitValue() < otherCard.getSuitValue():
                return True
            else:
                return False
        else:
            return False
    
    def __le__(self, otherCard):
        if self.getFaceValue() < otherCard.getFaceValue():
            return True
        elif self.getFaceValue() == otherCard.getFaceValue():
            if self.getSuitValue() <= otherCard.getSuitValue():
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, otherCard):
        if self.getFaceValue() > otherCard.getFaceValue():
            return True
        elif self.getFaceValue() == otherCard.getFaceValue():
            if self.getSuitValue() > otherCard.getSuitValue():
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, otherCard):
        if self.getFaceValue() > otherCard.getFaceValue():
            return True
        elif self.getFaceValue() == otherCard.getFaceValue():
            if self.getSuitValue() >= otherCard.getSuitValue():
                return True
            else:
                return False
        else:
            return False