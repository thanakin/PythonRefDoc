x = 5
y = "John"
print(x)
print(y)

x = 4 #x is of type int
x = "Sally" #x is now of type str
print(x)

x = "John"
# is the same as
x = 'John'

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z= "Orange"
print(x)
print(y)
print(z)


x = "awesome"
print("Python is " +  x)

x = "Python is "
y = "awesome"
z = x + y
print(z)


x = 5
y = 10
print(x + y)


x = "5"
y = "John"
print(x + y)

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()



x = "awesome"

def myfcunt():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)



def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)



x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is "  + x)
