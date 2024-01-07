#keyword based arguments
def my_funcn(**kwargs):
    print(kwargs)

my_funcn(name='ABC',age=32,name1="QWE")






def my_funcn(*args,**kwargs):
   # print(args)
    print(args)
    print(kwargs)

my_funcn("abc",hello ='ITM' ,name='ABC',age=32)
