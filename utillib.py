#! /usr/bin/env python
# from https://www.geeksforgeeks.org/python-program-for-bubble-sort/

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

if __name__ == '__main__':
    test = [64, 34, 25, 12, 22, 11, 90]
