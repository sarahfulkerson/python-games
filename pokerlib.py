#! /usr/bin/env python

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}

# Royal Flush - possible combos
royalflush = []
for s in sorted(suits.values()):
    l = []
    for v in values[-5:]:
        l.append('%s%s' % (v, s[0]))
    royalflush.append(l)

# Straight - possible combos
straight = []
for s in range(9):
    l = values[s:s+5]
    straight.append(l)

# Four of a Kind - possible combos
fourofakind =  []
for v in values:
    l = []
    for s in sorted(suits.keys()):
        l.append('%s%s' %(v,s))
    fourofakind.append(l)
# print(fourofakind)