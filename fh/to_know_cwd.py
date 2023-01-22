'''current working directory'''

import os

#to know the current working directory (cwd)
#cwd=os.getcwd()
#print("Current working directory: ",cwd)

#to create a folder
#os.mkdir("Personal")
#print("Personal directory created in cwd")

#to create directory in sub
#os.mkdir("Personal/files")
#print("mysubdir created inside mysub")

#to remove a directory
#os.rmdir("Personal/files")
#os.rmdir("Personal")

#os.makedirs("Personal/files")
#os.removedirs("Personal/files")

#to see content of cwd
print(os.listdir("."))
