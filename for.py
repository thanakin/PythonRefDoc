fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('\n')

for x in "banana":
  print(x)

print('\n - break Statement')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

print('\n')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

print('\n - continue Statement')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

print ('\n - range() Function')

for x in range(6):
  print(x)

print ('\n')

for x in range(2, 6):
  print(x)

print ('\n')

for x in range(2, 30, 3):
  print(x)

print ('\n - Else in For Loop')

for x in range(6):
  print(x)
else:
  print("Finally finished!")

print ('\n - Nested Loops')
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

print ('\n - pass Statement')
for x in [0, 1, 2]:
  pass
