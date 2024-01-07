# if we want to remove a file we have to take help from os module
import os
if os.path.exists("abc2.txt"):
    os.remove("abc2.txt")
else:
    print("This file is not there")

