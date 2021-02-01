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