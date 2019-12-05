print("Hello")
print('Hello')

a = "Hello"
print(a)

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

c = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

d = "Hello, World!"
print(a[1])

e =  "Hello World!"
print(b[2:5])

f = "Hello, World!"
print(b[-5:-2])

g = "Hello, World!"
print(len(a))

h = " Hello, World! "
print(h.strip()) # returns "hello, World!"

i = "Hello, World!"
print(i.lower())

j =  "Hello, World!"
print(j.upper())

k = "Hello, World!"
print(k.replace("H", "J"))

l = "Hello, World!"
print(l.split(",")) # returns ['Hello', ' World!']

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

txt2 = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

m = "Hello"
n = "World!"
o = m + n
print(o)

p = "Hello"
q = "World!"
r = p + " " + q
print(r)

'''
age = 36
txt = "My name is John, I am " + age
print(txt)
'''

age = 36
txt = "My name is John, I am  {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


'''txt = "We are the so-called "Vikings" from te north."'''
txt = "We are the so-called \"Vikings\" from the  north."

