
class Person:
    pass # we can pass for adding attributes of class
    def __init__(self,name,surname,birthyear):
        # attributes of object
        self.name= name 
        self.surname =surname
        self.birthyear=birthyear


p1= Person("Name","Surname",1999)

print(type(p1))
print(f"name: {p1.name}\nsurname: {p1.surname}")