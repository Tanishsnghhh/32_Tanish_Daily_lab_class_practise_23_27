str= "ITM SKILLS UNIVERSITY"
i=0

'''while i<len(str): #while loop
    print(str[i])
    i+=1'''

'''def fun(str,char):
    for i in str:
        if i==char:
            print("str charchater found at",str.index(i))
            break
        else:
            print("charachter not found")
        
        return fun

a = input("enter the word : ") 
fun(str,a'''

def func(str,char):
    for i in str:
        if i==char:
            print("str character found at",str.index(i))
            break
        else:
            print("character not found")
        return func
a = input("enter the word : ") 
func(str,a)