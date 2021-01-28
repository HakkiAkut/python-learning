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

import datetime as dt
print(dt.datetime.now().date())
print(dt.datetime.now().strftime("%A %d %B %Y"))

import os
print(os.name) # nt is windows
print(os.getcwd())
# os.chdir("C:\\") changes dir
# os.listdir("C:\\") lists files in C
# os.mkdir("name") creates dir
# os.system("notepad.exe")
print(os.path.abspath("modules.py"))
print(os.path.dirname(os.path.abspath("modules.py")))
# os.path.exists("c:\\python") checks is exist or not

import re
print(re.search("[A-Z]","hakki"))
# split(" ",str) splits str with " "
# findAll("py", str) finds py in str

# help('modules')
import termcolor  # pip install  termcolor
print(termcolor.__file__)
print(termcolor.colored("colored string",color="red",on_color="on_white",attrs=["bold"]))
