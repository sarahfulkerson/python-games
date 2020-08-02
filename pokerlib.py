#! /usr/bin/env python

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
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    def __eq__(self, other):
        return values.index(self.value) == values.index(other.value)
    def __ne__(self, other):
        return values.index(self.value) != values.index(other.value)
    def __gt__(self, other):
        return values.index(self.value) > values.index(other.value)
    def __ge__(self, other):
        return values.index(self.value) >= values.index(other.value)
    def __lt__(self, other):
        return values.index(self.value) < values.index(other.value)
    def __le__(self, other):
        return values.index(self.value) <= values.index(other.value)
    def getValue(self):
        return self.value
    def getSuit(self):
        return self.suit

class Deck:
    pass