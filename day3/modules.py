# pip install <package-name> command for installing libs 
import math as mt
# from math import * -> will let us use without imported file name(floor() rather than math.floor())
# from math import factoriel, sqrt ->  also we can import only specified methods
'''
value = dir(math) methods
print(value)
value = help(math) explenations
print(value)
'''
print(mt.floor(5.9))
print(mt.sqrt(23))

import random as rn
print(rn.random()) # 0 - 1
print(rn.uniform(10, 100)) # float
print(rn.randint(20,50)) # int
chars=["a","b","c","d","e"]
print(rn.choice(chars)) # takes one char randomly
rn.shuffle(chars) # shuffles list
print(chars)
print(rn.sample(chars,3)) # takes 3 random chars

# import own module
import mymodule as mm
print(mm.sumOfN(11))