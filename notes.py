class Testclass:
    def __init__(self):  #constructor function using self
        self.name = None #variable using self
        self.age = None#variable using self
        self.dept = None
#Test array = []#empty array

objs=list()
for i in range (10):
    objs.append(Testclass())

print(objs)

objs[0].name = "ABC"
objs[0].age = 18

print(objs[0].name)
print(objs[0].age)