#! /usr/bin/env python
# from https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubbleSort(arg):
    """
    Takes a list and returns a bubble-sorted list.
    """
    l = arg[:]
    n = len(l)

    for i in range(n-1):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    return l

if __name__ == '__main__':
    test = [64, 34, 25, 12, 22, 11, 90]
    res = bubbleSort(test)
    print('Sorted array is: ')
    for i in range(len(res)):
        print('%s' % res[i])