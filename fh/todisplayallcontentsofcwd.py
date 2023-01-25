#to display all contents of cwd
import os
from os import *
for dirpath,dirnames,filenames in walk('D:\AnupaCC\Python'):
    print ("Current working directory path: ",dirpath)
    print("Directories: ",dirnames)
    print("Files: ",filenames)
    print()
