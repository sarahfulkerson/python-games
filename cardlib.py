#! /usr/bin/env python

from utillib import bubbleSort

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}
royalflush = []
straight = []
fourofakind =  []

# Royal Flush - possible combos
for s in sorted(suits.values()):
    l = []
    for v in values[-5:]:
        l.append('%s%s' % (v, s[0]))
    royalflush.append(l)

# Straight - possible combos
for s in range(9):
    l = values[s:s+5]
    straight.append(l)

# Four of a Kind - possible combos
for v in values:
    l = []
    for s in sorted(suits.keys()):
        l.append('%s%s' %(v,s))
    fourofakind.append(l)
# print(fourofakind)

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
        Defaults to False.
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
        Sorts the Hand in place using bubble sort.
        """
        sorted_hand = bubbleSort(self.hand)
        self.card1 = sorted_hand[0]
        self.card2 = sorted_hand[1]
        self.card3 = sorted_hand[2]
        self.card4 = sorted_hand[3]
        self.card5 = sorted_hand[4]
    def __getitem__(self, index):
        """Fetches the Card at the given index."""
        return self.hand[index]
    def __iter__(self):
        """
        Returns an instance of iterator class 'hand_iterator'.
        """
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

if __name__ == '__main__':
    a = Card(2, 'd')
    b = Card('7', 'd', suitRank=True)
    c = Card('4', 'C')
    d = Card('a', 's')
    e = Card('q', 'd')
    h = Hand(a, b, c, d, e)
    print('repr:\n', repr(h))
    print('suitRank, h[0] = ', h[0].getSuitRank())
    print('h[0]: ', type(h[0]), ', ', h[0])
    print('suitRank, h[1] = ', h[1].getSuitRank())
    print('h[1]: ', type(h[1]), ', ', h[1])