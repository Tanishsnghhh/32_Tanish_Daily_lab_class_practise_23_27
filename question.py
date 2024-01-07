#1enter name between the lines
'''def my_funcn(*args,**kwargs):
    print(*args)
    print(kwargs)
n=(input("enter your name"))

my_funcn("welcome"  ,n, "to ITM")
'''

import random
x=[]
def my_funcn(**kwargs):
    #print(kwargs)
    random_number = random.randint(1, 100)
    while  random_number in x :
        random_number = random.randint(1, 100)
    print("unique roll no",random_number)
    for i in kwargs:
        print(i,'=',kwargs[i])

n=(input("enter your name : "))
a=(input("enter your age : "))
e=(input("enter your email : "))
my_funcn(name=n,AGE=a,email=e)

