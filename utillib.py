#! /usr/bin/env python
# from https://www.geeksforgeeks.org/python-program-for-bubble-sort/

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}

def sortedOnIndex(val, ind):
    """
    Uses bubble sort to return a sorted list of values from a list of 
    unsorted values, using a passed in index.
    """
    vls = val[:]
    for i in range(len(vls)-1):
        for j in range(0, len(vls)-i-1):
            if ind.index(vls[j]) > ind.index(vls[j+1]):
                vls[j], vls[j+1] = vls[j+1], vls[j]
    return vls
def sortMultipleLists(list1, list2, *pargs):
    """
    Uses bubble sort to sort multiple lists in place based on the sort
    results of list1. If all lists are not the same length as list1, an
    exception will be thrown.
    """
    others = list(*pargs)
    for i in range(len(list1)-1):
        for j in range(0, len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
                list2[j], list2[j+1] = list2[j+1], list2[j]
                if others:
                    for listn in others:
                        listn[j], listn[j+1] = listn[j+1], listn[j]    
if __name__ == '__main__':
    pass
    # test = [64, 34, 25, 12, 22, 11, 90]
