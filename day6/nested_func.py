def outer(num):
    print(num)
    #encapsulation
    def inner(num):
        print("inner")
        return num+1
    print(inner(num)) #need to call inner func inside outer func 
outer(10)
# cant call inner outside of outer

def factorial(num):
    def inner_fact(num):
        if num <= 1:
            return 1
        else:
            return num * inner_fact(num-1)
    return inner_fact(num)

print(factorial(6))


#function returning
def power(num):
    def inner(pow):
        return num ** pow
    return inner
print(power(3)(3))

#function as param
def operation(func1,func2,op_name,value):
    if op_name =="sqrt":
        return func1(value)
    elif op_name =="power":
        return func2(value,2)
    else:
        raise Exception("operation name must be sqrt or power!")
import math
print(operation(math.sqrt,math.pow,"power",3))