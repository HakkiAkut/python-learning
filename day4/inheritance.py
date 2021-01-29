class Person():
    className="Person"
    @classmethod
    def nameOfClass(cls):
        return f"class name: {cls.className}"
    person_count=0
    def __init__(self,name):
        self.name= name
        Person.person_count +=1

    def myClass(self):
        return "I'm a person"

class Student(Person):
    @classmethod
    def addPerson(cls,data):
        name,student_no=data.split(',')
        return cls(name,student_no)

    def __init__(self,name,student_no):
        Person.__init__(self,name)
        self.student_no=student_no

    def myClass(self):
        return "I'm a student"
p2=Person("a")
p1= Student(name="hakki",student_no=11111)
print(p1.name,p1.student_no)
print(p1.myClass())
print(Person.person_count)
print(Person.nameOfClass())

p3 = Student.addPerson("Hakki,22222")
print(p3.name)
