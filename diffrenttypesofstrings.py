#diffrent types of strings

print('Hi, what\'s up?') 
print("Hi,\"what's up?") #\- escape sequence(eg- \n for newline, \t- tabspace)
print(r"""Hi,"what's up?""") #r- raw string, can't use escape sequences with r string 
print("Welcome to {},{}".format("ITM","Kharghar")) #.format() is used to to send arguments to the parameters in the string(default- positional arguments)
print("Welcome to {1},{0}".format("Kharghar","ITM")) #.format() is used to send keyword based arguments

a=input("Enter your name: ")
print("Hello {}".format(a))