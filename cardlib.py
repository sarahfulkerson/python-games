#! /usr/bin/env python3
# https://projecteuler.net/problem=54

# TODO: abstract base classes!
from utillib import sortedOnIndex

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}

def makeCardDict(hand):
    carddict = {}
    # make a dictionary of suits in the Hand, and make the values of the keys the set of Card values in those suits
    for card in hand:
        s = card.getSuit()
        if carddict.get(s) == None:
            carddict[s] = {card.getValue()}
        else:
            carddict[s].add(card.getValue())
    return carddict

def isRoyalFlush(hand):
    """Returns True if the passed in Hand is a royal flush."""
    handvalues = sortedOnIndex(hand.getValues(), values)
    royalflushvalues = values[-5:]
    return handvalues == royalflushvalues and len(hand.getSuits(distinctsuits=True)) == 1

def isStraight(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a straight and false if it is
    not. The second value in the list will be the high card in the
    straight, or None if the Hand is not a straight.
    """
    handvalues = sortedOnIndex(hand.getValues(), values)
    straight = []
    # take a slice of the list the same length as the Hand and see if the values match
    for s in range(len(values)-len(handvalues)+1):
        straight = values[s:s+len(handvalues)]
        if straight == handvalues:
            return [True, straight[-1]]
    else:
        return [False, None]

def isFourOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is four of a kind and false if 
    it is not. The second value in the list will be the value of
    the four of a kind, or None if the Hand is not four of a kind.
    """
    fourofakind = makeCardDict(hand)
    
    # if there are less than 4 suits in fourofakind then the Hand cannot be four of a kind
    if len(fourofakind) < 4:
        return [False, None]
    
    vals = list(fourofakind.values())
    res = vals[0].intersection(vals[1], vals[2], vals[3])

    if len(res) == 0:
        return [False, None]
    elif len(res) == 1:
        return [True, list(res)[0]]
    else:
        assert False, 'too many cards!'

def isFlush(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a flush and false if it is 
    not. The second value in the list will be the value of the 
    high card in the flush, or None if the Hand is not a flush.
    """
    handvalues = sortedOnIndex(hand.getValues(), values)
    handsuits = hand.getSuits(distinctsuits=True)
    if len(handsuits) == 1:
        return [True, handvalues[-1]]
    else:
        return [False, None]

def isStraightFlush(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a straight flush and false if 
    it is not. The second value in the list will be the value of 
    the high card in the straight flush, or None if the Hand is 
    not a straight flush.
    """
    straight = isStraight(hand)
    flush = isFlush(hand)
    if straight[0] and flush[0]:
        return straight
    else:
        return [False, None]

def isFullHouse(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is a full house and false if it 
    is not. The second value in the list will be the value of the 
    high card in the full house, or None if the Hand is not a 
    full house.
    """
    fullhouse = makeCardDict(hand)
    highcard = sortedOnIndex(hand.getValues(), values)[-1]
    res = {}
    for suit in fullhouse:
        for val in fullhouse[suit]:
            if res.get(val) == None:
                res[val] = 1
            else:
                res[val] += 1
    # if len(res) != 2 then there are more than 3 card values in the hand, so a full house is impossible
    if len(res) != 2:
        print('first: ', res)
        return [False, None]
    
    counts = sorted(list(res.values()))
    # if 1 of the values in res appears in 3 suits and the other value appears in 2 suits
    # then the Hand is valid
    if counts[0] == 2 and counts[1] == 3:
        return [True, highcard]
    else:
        assert False, 'not enough suits!'

def isThreeOfAKind(hand):
    """
    Returns a list with 2 values. The first value in the list will 
    be True if the passed in Hand is three of a kind and false if 
    it is not. The second value in the list will be the value of
    the three of a kind, or None if the Hand is not three of a kind.
    """
    threeofakind = makeCardDict(hand)

    return threeofakind

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
    def getValues(self, *, distinctvalues=False):
        """
        Returns the values of all Cards in the Hand.
        """
        v = []
        if distinctvalues == True:
            for c in self.hand:
                val = c.getValue()
                if val not in v:
                    v.append(val)
        else:
            for c in self.hand:
                v.append(c.getValue())
        return v
    def getSuits(self, *, distinctsuits=False):
        """
        Returns the suits of all Cards in the Hand.
        """
        s = []
        if distinctsuits == True:
            for c in self.hand:
                val = c.getSuit()
                if val not in s:
                    s.append(val)
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

if __name__ == '__main__':
    a = Card('2', 'd')
    b = Card('2', 's')
    c = Card('2', 'c')
    d = Card('q', 'h')
    e = Card('q', 'd')
    h = Hand(a, b, c, d, e)
    #print('isThreeOfAKind: %s\nisStraight: %s\nisFlush: %s\nisFullHouse: %s\nisFourOfAKind: %s\nisStraightFlush: %s\nisRoyalFlush: %s' 
    #    % (isThreeOfAKind(h), isStraight(h), isFlush(h), isFullHouse(h), isFourOfAKind(h), isStraightFlush(h), isRoyalFlush(h)))
    print(isThreeOfAKind(h))