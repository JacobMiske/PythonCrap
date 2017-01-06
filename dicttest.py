# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 22:22:07 2017

@author: LENOVO USER
"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for dict_keys in aDict:
        result += 1
    return result


animals = {'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}

animals['d'] = 'donkey'

print(how_many({'a': 'aardvark', 'b': 'baboon', 'c': 'coati'}))
