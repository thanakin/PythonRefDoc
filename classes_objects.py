class MyClass:
  x = 5
  print(x, '\n')


p1 = MyClass()
print(p1.x, '\n')

print('__init__() Function')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print('\nObject Methods')

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()



print('\nself Parameter')

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

print('\nModify Object Properties')
p1.age = 40

print('\nDelete Object Properties')
del p1.age

print('\nDelete Objects')
del p1

print('\npass Statement')
class Person:
  pass
