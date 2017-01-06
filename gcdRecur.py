# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 23:05:37 2016

@author: LENOVO USER
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdRecur(b, a % b)

print(gcdRecur(15, 12))