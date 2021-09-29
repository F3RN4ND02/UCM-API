
def function1():
    var1 = input("writesomething1")
    var2 = input("write something 2")
    var3 = input("write something 3")
    return var1, var2, var3

def function2(var1, var2, var3):
    print(var1 + var2 + var3)
    
var1, var2, var3 = function1()
function2(var1, var2, var3)

#a=25
a = None
print(a)
