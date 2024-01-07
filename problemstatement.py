#wap to count number of vowels in a given string considering both upper case and lower case.
'''string={a,e,i,o,u,A,E,I,O,U}
s=0
str=input("to cheack vowels")
if string==s:
    print( " it is a match " )
    s+=1
else:
    print( " it is not a match " )
'''

'''
vowel = ["A","E","I","O","U"]

a = input("Enter the word : ")

count = 0

for i in a:
    if i.upper() in vowel:
        count+=1
    
print(count)
'''

#2 wap that takes a sentence as input and counts number of words in it.
'''
a = input("Enter the sentence :")

count = 1

for i in a:
    if(i == " "):
        count+= 1

print(count)
'''


#wap to check if two strings are anagrams of each other.

'''str1=input("1st: ")
str2=input("2nd: ")
a=sorted(str1)
b=sorted(str2)
if a==b:
    print(str1,"&",str2,"are anagram")
else:
    print(str1,"&",str2,"are not anagram")'''




#wap that converts camel case string to snake case.
a = input("Enter  : ").split(" ")
for i in range(0,len(a)):
    str1 = ""
    for j in range(0,len(a[i])):
        
        if(a[i][j] == a[i][j].upper()):
            if(j == 0):
                str1 += a[i][j]
            else:
                str1 += "_" + a[i][j].lower()
        else:
            str1 += a[i][j]
    
    a[i] = str1


for i in a:
   print(i,end=" ")


#wap that takes a list of strings as input and sorts them based on their length.

'''a = input("enter : ").split(" ")
print(a)

for i in range(0,len(a)):
    for j in range(i,len(a)):

        if(len(a[i]) > len(a[j])):
            temp = a[j]
            a[j] = a[i]
            a[i] = temp

for i in a:
    print(i , end = " ")'''