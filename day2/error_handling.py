import re
# exceptions
try:
    a,b=(5,"0")
    print(a/b)
except ZeroDivisionError:
    print("can't divide to 0")
except TypeError as e:
    print("Error:\n",e)
try:
    a,b=(5,1)
    print(a/b)
except: 
    print("error")
else:
    print("correct usage")
finally:
    print("same as java")

# raise exception
pwd=input("pwd: ")
def pwd_check(pwd):
    if(len(pwd)<6):
        raise Exception("pwd must be greater or equal than 8")
    elif not re.search("[a-z]",pwd):
        raise Exception("pwd must contain lower case character")
    elif not re.search("[A-Z]",pwd):
        raise Exception("pwd must contain upper case character")
    elif not re.search("[0-9]",pwd):
        raise Exception("pwd must contain number")
    else:
        print("pwd accepted")

try:
    pwd_check(pwd)
except Exception as e:
    print(e)

# can use raise ValueError("error") as well as other exceptions