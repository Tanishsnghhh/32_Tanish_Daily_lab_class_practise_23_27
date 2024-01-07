#types of function
'''def my_funcn(*args):
    for i in args:
       # print(i,end=" ")
        for j in i:
            tsum+=j
    print ("\nsum:",tsum)'''

def myfunction(*args): 
    tsum=0
    for i in args:
        #print(i,end=' ')
        for j in i:
            print(j,end=' ')
            tsum+=j
    print("\nSum:",tsum)
a=[]
n=int(input("Enter a number(0 to exit): "))
while n!=0:
    a.append(n)
    n=int(input("Enter a number(0 to exit): "))
print(a)
myfunction(a)