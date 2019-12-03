def myfunc():
  x = 300
  print(x)
myfunc()

print('\n Function Inside Function \n')
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

print('\n Global Scope \n')
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

print('\n Naming Variables \n')
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()
print(x)


print('\n Global Keyword \n')
def myfunc():
  global x
  x = 300

myfunc()
print(x)


x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)