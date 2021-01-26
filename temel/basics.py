# print
print("python")
print(2+5)
# data types
ph="python" 
integer=21
boolean =True
print(ph)
print(integer)
print(boolean)
# string
print(ph + "boolean")
print(ph[2])
print(ph[len(ph)-1])
print(ph[2:len(ph)-1])
print(ph[2:len(ph):2]) # takes one string every 2 char from 2 to end
name="Hakki"
surname="Akut"
# string formatting
print("name surname {} {}".format(name,surname)) 
print("name surname {x} {y}".format(x=name,y=surname)) 
result=100/1211
print("name surname {x:1.3} ".format(x=result)) 
# string methods
print(name.upper())
str1="name surname"
print(str1.title())
print(str1.capitalize())
print(str1.replace(" ",","))

# inputs
x = input("x: ")
print(type(x))
print(type(int(x)))

x=int(input("input: "))
x1,x2= (3.14*2*x,3.14*(x**2))
print("x1= "+str(x1)+", x2= "+str(x2))


