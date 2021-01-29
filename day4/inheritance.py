class Person():
    def __init__(self,name):
        self.name= name
    def myClass(self):
        return "I'm a person"

class Student(Person):
    def __init__(self,name,student_no):
        Person.__init__(self,name)
        self.student_no=student_no
    def myClass(self):
        return "I'm a student"

p1= Student(name="hakki",student_no=11111)
print(p1.name,p1.student_no)
print(p1.myClass())
