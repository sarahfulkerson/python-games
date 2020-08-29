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

def _valueMethodCustomizer(dic, oper, desiredlen, desiredcount, *, appendon=False):
    """
    dic = the passed in result of countOfValues()
    oper = the desired operator to use to compare dic to the value of desiredlen
    desiredlen = the length to use when comparing the length of dic with the operator passed in to oper
    desiredcount = the desired number of times a value should show up in the hand
    appendon = whether or not to append multiple values that match the desiredcount to the result set; defaults to False
    """
    if appendon == False:   # if appendon == False then res is a string
        res = ''
    else:                   # else res is a list
        res = []
    evalbuilder = 'len(%s) %s %s' % (dic, oper, desiredlen) # builds the string for the eval

    if eval(evalbuilder):       # gets the length of the passed in countOfValues dict and compares it using the passe din operator to the desired values dict length
        return False    # return if the hand cannot be the desired rank due to the incorrect number of values in the hand

    vals = list(dic.items())    # make a list of the countOfValues items    
    
    for x in vals:                  # for each key/value pair in the 'vals' list...
        if x[1] == desiredcount:    # if the count of that value equals the desired count...
            if appendon == False:       # and if appendon == False...
                res = x[0]                  # set 'res' equal to that value
            else:                       # else appendon == True...
                res.append(x[0])            # so append the value to res


    if appendon == False and len(res) == 1:
        return [True, res]
    elif appendon == True and len(res) != 0:
        l = sortedOnIndex(res, values)
        return [True, l]
    else:
        return False
    
if __name__ == '__main__':
    pass
    # test = [64, 34, 25, 12, 22, 11, 90]
