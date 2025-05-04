# Scope of a variable.

"""
global scope --> file level ==> ex : a = 4 

local scope --> function level ==> ex : def sum : 
                                            a = 3
                                            print(a)
                                            
nonlocal keyword --> used to tell to interpreter that the variable is belongs to the outer function.

global keyword --> used to tell to interpretor thaat the variable is belongs to the file level.

"""
"""

global level --> 

a = 45

def update():
    global a 
    a = 0
    a = a + 3

update()

def update2():
    global a
    a = 34

update2()

print(a)

"""
# Local scope --> Function scope both are same

"""
def swap(a,b):
    temp  = a
    print(temp)
    a = b
    b = temp



a = 34
b = 45

swap(a,b)
print(a)
print(b)

# print(temp)

"""

# Inner Scope --> nested level functions


a = 45

def moreOut():
    global a
    a = -34

    def outer():
        x = 32 
        a = 45

    # nested function.
        def inner():
            nonlocal a 
            print(a) # 45
            nonlocal x
            x = 34
            print(x) # 34
    

        print(x,a) # 32 , 45
        inner() # called
        print(x,a) # 34 , 45 

    print(a) # -34 
    outer()

moreOut()

