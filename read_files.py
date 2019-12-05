print('\n File Open')
f = open("demofile.txt", "r")
print(f.read())

print('\n Read Only Parts of the File')

f = open("demofile.txt", "r")
print(f.read(5))

print('\n Read Lines')

f = open("demofile.txt", "r")
print(f.readline())

print('\n')

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

print('\n')

f = open("demofile.txt", "r")
for x in f:
  print(x)

print('\n Close Files')

f = open("demofile.txt", "r")
print(f.readline())
f.close()