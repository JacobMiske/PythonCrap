# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:34:43 2017

@author: LENOVO USER
"""

"""
animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print(animals.values())
"""

'''
def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return(rem(x - a, a))

print(rem(152, 4))
'''

"""
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")

print(fancy_divide([0, 2, 4], 0))
"""
'''
def Square(x):
    print(x ** 2)
print(Square(2))
'''
"""
stuff =["iBoy", "iQ", "iPaid"]
for thing in stuff:
    if thing == 'iQ':
        print("Found it")
"""
"""
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0
    index = 0
    for index in range(len(listA))
        result += (listA[index] + listB[index])
        index += 1
    return result
"""
'''
def is_list(p):
    return isinstance(p, list)

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    L.reverse()
    for i in L:
        if is_list(i):
            deep_reverse(i)

L = [[0, 1, 2], [1, 2, 3], [3, 2, 1], [10, -10, 100]]
print(deep_reverse(L))
'''
"""
def f(a, b):
    return a>b

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    intersect = d1.keys() & d2
    difference = d1.keys() ^ d2
    a = {i: f(d1[i], d2[i]) for i in intersect}
    b = {i: d1[i] for i in difference & d1.keys()}
    return a, b
"""

'''
def dict_interdiff(d1, d2):
    # find keys that are in one dict but not both
    difference = d1.keys() ^ d2.keys()
    # intersection, keys that are common to d1 and d2.
    intersect = d1.keys() & d2.keys()
    # apply f on values of the keys that common to both dicts.
    a = {k: f(d1[k], d2[k]) for k in intersect}
    b = {k: d1[k] for k in difference & d1.keys()}
    # add key/value pairings from d2 using keys that appear in sym_diff
    b.update({k: d2[k] for k in difference & d2.keys()})
    return a,b

print(dict_interdiff({1:24,2:13,3:10}, {1:2,2:1,4:15}))
'''
"""
def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''
    if isinstance(aList, list):
        return aList.append(map(flatten, aList))
    else:
        return aList
"""
"""
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    newList = []
    for i in aList:
        if isinstance(i, int or str):
            newList.append(i)
        elif isinstance(i, list):
            return sum(map(flatten, l))
        else:
            return l
"""
'''
def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el
'''
"""
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    return flatten(aList[0]) + (flatten(aList[1:]) if len(aList) > 1 else []) if type(aList) is list else [aList]

print(flatten([[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]))
"""
'''
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

print(Square(50))
'''


L = [0, -10, 5, 6, -4]
print(L[0:3])