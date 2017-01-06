# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:11:56 2016

@author: LENOVO USER
"""


def isIn(char, aStr):
    if aStr == '':  # Check for empty string
        return False
    m = aStr[len(aStr) // 2]
    if char == m:
        return True
    elif len(aStr) == 1:
        return False
    else:
        if char < m:
            return isIn(char, aStr[:len(aStr) // 2])
        elif char > m:
            return isIn(char, aStr[len(aStr) // 2:])
    return isIn(char, aStr)
    
print(isIn(a, abc))
