#! /usr/bin/env python3
# https://projecteuler.net/problem=54

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}
fourofakind =  []

def _setup_():
    '''
    Helper function to fill out the top-level list attributes above.
    '''

    # Four of a Kind - possible combos
    for v in values:
        l = []
        for s in sorted(suits.keys()):
            l.append('%s%s' %(v,s))
        fourofakind.append(l)

def isRoyalFlush(hand):
    """Returns True if the passed in Hand is a royal flush."""
    handvalues = sortedCardValues(hand.getValues())
    royalflushvalues = values[-5:]
    return handvalues == royalflushvalues and len(hand.getSuits(distinctsuits=True)) == 1

def isStraight(hand):
    """Returns True if the passed in Hand is a straight."""
    handvalues = sortedCardValues(hand.getValues())
    straight = []
    # Straight - possible combos
    for s in range(len(values)-len(handvalues)+1):
        straight = values[s:s+len(handvalues)]
        if straight == handvalues:
            return True
    else:
        return False

def sortedCardValues(v):
    """Returns a sorted list of Card values from a passed in list of unsorted values."""
    vls = v[:]
    n = len(vls)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if values.index(vls[j]) > values.index(vls[j+1]):
                vls[j], vls[j+1] = vls[j+1], vls[j]
    return vls

class Card:
    """
    Represents a playing card in a card game.

    Attributes:
    
    value
        Holds the value of the card. 
        Available values: '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'

    suit
        Holds the suit of the card. 
        Available values: 'C', 'D', 'H', 'S'

    suitRank
        When True, all relational operators will consider both values and suits in comparisons.
        When False, all relational operators will consider only values in comparisons.
        Defaults to False. 'suitRank=True' still needs implementation.
    """
    def __init__(self, value, suit, suitRank=False):
        self.value = str(value).upper()
        self.suit = suit.upper()
        self.suitRank = suitRank
    def getValue(self):
        """Returns the value of 'value'."""
        return self.value
    def getSuit(self):
        """Returns the value of 'suit'."""
        return self.suit
    def getSuitRank(self):
        """Returns the value of 'suitRank'."""
        return self.suitRank
    def __eq__(self, other):
        """
        self == other
        
        Returns true if the Cards are equal.
        """
        if self.suitRank == False:
            return values.index(self.value) == values.index(other.value)
        else:
            pass
    def __ne__(self, other):
        """
        self != other
        
        Returns true if the Cards are not equal.
        """
        if self.suitRank == False:
            return values.index(self.value) != values.index(other.value)
        else:
            pass
    def __gt__(self, other):
        """
        self > other
        
        Returns true if the Card 'self' is greater than Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) > values.index(other.value)
        else:
            pass
    def __ge__(self, other):
        """
        self >= other
        
        Returns true if the Card 'self' is greater than or equal to Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) >= values.index(other.value)
        else:
            pass
    def __lt__(self, other):
        """
        self < other
        
        Returns true if the Card 'self' is less than Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) < values.index(other.value)
        else:
            pass
    def __le__(self, other):
        """
        self <= other
        
        Returns true if the Card 'self' is less than or equal to Card 'other'.
        """
        if self.suitRank == False:
            return values.index(self.value) <= values.index(other.value)
        else:
            pass
    def __repr__(self):
        return "%s('%s', '%s')" % (self.__class__.__name__, self.value, self.suit)
    def __str__(self):
        return "%s: value = '%s', suit = '%s'" % (self.__class__.__name__, self.value, suits.get(self.suit))

class Hand:
    """
    This class takes 5 instances of class Card as arguments.

    Attributes:
    -- card1 (instance of class Card)
    -- card2 (instance of class Card)
    -- card3 (instance of class Card)
    -- card4 (instance of class Card)
    -- card5 (instance of class Card)
    -- hand (list of 5 Card instances above)
    -- sort (method for sorting Hand in place)
    """
    def __init__(self, card1, card2, card3, card4, card5):
        self.card1 = card1
        self.card2 = card2
        self.card3 = card3
        self.card4 = card4
        self.card5 = card5
        self.hand = [card1, card2, card3, card4, card5]
    def sort(self):
        """
        Sorts the Hand in place in ascending order and return None.
        """
        hand = self.hand[:]
        n = len(hand)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if hand[j] > hand[j+1]:
                    hand[j], hand[j+1] = hand[j+1], hand[j]
        self.card1, self.card2, self.card3, self.card4, self.card5 = hand[0], hand[1], hand[2], hand[3], hand[4]
    def getValues(self):
        """
        Returns the values of all Cards in the Hand.
        """
        values = []
        for c in self.hand:
            values.append(c.getValue())
        return values
    def getSuits(self, distinctsuits=False):
        """
        Returns the suits of all Cards in the Hand.
        """
        s = []
        if distinctsuits == True:
            for c in self.hand:
                if c.getSuit() not in s:
                    s.append(c.getSuit())
        else:
            for c in self.hand:
                s.append(c.getSuit())
        return s
    def __getitem__(self, index):
        """Fetches the Card at the given index."""
        return self.hand[index]
    def __len__(self):
        """Returns the length of 'self.hand'."""
        return len(self.hand)
    def __iter__(self):
        """Returns an instance of iterator class 'hand_iterator'."""
        return hand_iterator(self.hand)
    def __repr__(self):
        return '%s(%s, %s, %s, %s, %s)' % (self.__class__.__name__,  repr(self.card1), repr(self.card2), repr(self.card3), repr(self.card4), repr(self.card5))
    def __str__(self):
        return '%s:\ncard1 = [%s],\ncard2 = [%s],\ncard3 = [%s],\ncard4 = [%s],\ncard5 = [%s]' % (self.__class__.__name__,self.card1, self.card2, self.card3, self.card4, self.card5)

class hand_iterator:
    """
    Iterator returned for the Hand iterable class.
    """
    def __init__(self, hand):
        self.hand = hand
        self.counter = 0
    def __next__(self):
        """
        Returns the next Card in the Hand until the Hand is empty.
        """
        if self.counter == len(self.hand):
            raise StopIteration
        n = self.hand[self.counter]
        self.counter += 1
        return n

class Deck:
    pass

_setup_()

if __name__ == '__main__':
    a = Card('2', 'd')
    b = Card('3', 'd')
    c = Card('4', 'd')
    d = Card('5', 'd')
    e = Card('6', 'd')
    h = Hand(a, b, c, d, e)
    print("straight: ", isStraight(h))