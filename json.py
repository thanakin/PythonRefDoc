'''
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.load(x)
# the result is a Python dictionary:
print(y["age"])
'''

'''
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
'''

'''
You can convert Python objects of the following types, into JSON strings:

dict
list
tuple
string
int
float
True
False
None
'''

'''
import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''

'''
When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:
Python	    JSON
dict	    Object
list	    Array
tuple	    Array
str	        String
int	        Number
float   	Number
True    	true
False	    false
None    	null
'''

'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))
'''
