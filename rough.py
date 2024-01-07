# '''class person:
#     def getdata(self):
#         self.name="tanish"
#         self.age=33
#     def gender(self):
#         self.gender="male"
#     def colour(self):
#         self.colour="white"

# print ()'''



# class Greet():
#     def sayhello(self):
#         print("hello welcome here")

# greeting=Greet()
# greeting.sayhello()


class person():
    def __init__ (self):
        self.age = 0
        self.colour = "none"

    def getdata(self):
        print(self.age,self.colour)

    def setdata(self):
        self.age = int(input("enter age "))
        self.colour = (input("enter colour "))


obj = person()
obj.getdata()
obj.setdata()
obj.getdata()



