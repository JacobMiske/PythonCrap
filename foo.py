# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 12:42:27 2016

@author: LENOVO USER
"""

"""P1
x = 'pi'
y = 'pie'

x, y = y, x

print(x)


print(y)
"""

"""P2
def f(x):
    while x > 3:
        f(x+1)

f(4)
"""

"""
varB = 3
varA = 'hi'

if type(varA) and type(varB) == type('ha'):
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')
else:
    print('not equal')
"""

"""
num = 2
while num <= 10:
    print(num)
    num += 2
print('Goodbye!')
"""
"""
end = 19

num = 1
total = 0
while total < end:
    total = num + 1

print(total)
"""

"""
school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print(char)
    else:
        numCons -= 1

print('numVowels is: ' + str(numVowels))
print('numCons is: ' + str(numCons))
"""

"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0

    for key in aDict:
        result += len(aDict[key])
    return result

animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))
"""

def biggest(aDict):
