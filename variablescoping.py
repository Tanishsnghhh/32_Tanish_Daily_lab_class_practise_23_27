#GLOBALLOCALVARIABLE
'''var_global = 4
def func():
    var_global=3
    print(var_global)
func()
print(var_global)
'''

#GLOBALNONLOCALLOCAL
var1=10 
def func():
    var1=3
    print(var1)
    def fun2():
        nonlocal var1
        var1=4
    print(var1)
    fun2()
func()
print(var1)
