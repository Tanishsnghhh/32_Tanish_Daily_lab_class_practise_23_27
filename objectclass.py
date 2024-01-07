#default constrctor
'''class Student:

    def __init__(self):
        self.name="ABC"
        self.age=18
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
obj=Student()
obj.display()
'''

#partmitrized cons
'''class Student:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("constructor is called")
    def display(self):
        print("name:",self.name)
        print("age:",self.age)


obj=Student("ABC",18)
obj.display()
obj1=Student("xyz",30)
obj1.display()
'''

#count number of student
'''class Student:

    count =0 

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("constructor is called")
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        
        Student.count=Student.count+1

obj=Student("ABC",18)
obj.display()
obj1=Student("xyz",30)
obj1.display()
print(Student.count)'''

