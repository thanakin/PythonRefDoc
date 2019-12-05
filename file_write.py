'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:

"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

print('\n')


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

print('\n')

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")

#Create a new file if it does not exist:
f = open("myfile.txt", "w")