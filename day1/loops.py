import random
# operators

x,y=1,2
x,y=(y,x)
print(x,y)
## generally same as java == != < > <= >=, 'and' for && also 'or' for || and there is 'not' operator
## 'is' for idententity 'in' for  membership

# if elif else 
if x<y:
    print("true")
elif x==y:
    print("equal") 
else:
    print("false")

dic= {
    1:"one",
    2:"two",
    3:"three",
}

# loops
for key,value in dic.items():
    print(key,value)
x=0
y=0
while x < 100:
    y +=x
    x +=1
print(y)

q = ''
while not q:
    q="not null"
print(q)
# break and continue same as java

# loop methods
t=0
for x in range(0,100,5):
    t +=x
print(t)

for x,y in enumerate("loop"):
    print(x,y)

list1=[1,2,3]
list2=["one","two","three"]

for x,y in list(zip(list1,list2)):  # zip combines lists with index numbers
    print(x,y)

# list comprehentions
for x in range(4):
    print(x)
num=[x for x in range(4)]
print(num)
num1=[x for x in range(10) if x%2==0]
print(num1)
num2=[(x,y) for x in range(4) for y in range(4)]
print(num2)

# random 
f = random.randint(1,100)
print(f)