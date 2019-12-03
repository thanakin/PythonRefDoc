print('Use a Module')
import mymodule
mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

print('\nRe-naming a Module')
import mymodule as mx
a = mx.person1["age"]
print(a)


print('\nBuilt-in Modules')
import platform
x = platform.system()
print(x)

print('\n Using the dir() Function')
import platform

x = dir(platform)
print(x)


print('\nImport From Module')
from mymodule import person1
print (person1["age"])