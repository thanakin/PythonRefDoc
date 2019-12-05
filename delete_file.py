'''
Delete a File
To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("demofile.txt")
'''
import os

if os.path.exists("demofile0.txt"):
  os.remove("demofile0.txt")
else:
  print("The file does not exist")

#Remove the folder "myfolder":
os.rmdir("myfolder")