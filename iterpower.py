# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 20:37:04 2016

@author: LENOVO USER
"""

def iterPower(base, exp):
    result = 1
    while exp <= 0:
        result *= base
        exp -= 1
        return base * iterPower(base, exp -1)
    
    
