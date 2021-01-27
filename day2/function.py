
def sum1(a=1,b=8):
    '''
    DOCSTRING: returns sum of a and b
    '''
    return sum([a,b])
# help(sum) returns docstring
print(sum1(a=4))

def sum2(*params): # **params for dictionary
    return sum((params))
print(sum2(2,1,5,2,4,1))

def func(a,b, *params, **dict_params):
    print(a)
    print(b)
    print(params)
    print(dict_params)
func(1,2,3,4,5, one='one' ,two='two')

def charNum(word):
    return { letter: word.count(letter) for letter in word }

print(charNum("deneme"))

def square(a): return a**2
print(square(4))
num=range(5)
# map
res=list(map(square,num)) 

# lambda
res2= list(map(lambda num: num**2,range(6)))
square2 =lambda num: num**2
res3= list(map(square2,range(3)))
print(res)
for item in res2:
    print(item)
print(res3)

# filter
even=lambda num: num%2==0
print(list(filter(even,range(10))))