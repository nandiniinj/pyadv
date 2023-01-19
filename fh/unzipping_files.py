from zipfile import *

f=ZipFile("files.zip","r",ZIP_STORED)
names=f.namelist()

print(names)

for name in names:
    print("File name: ",name)
    print("The content of this file is:")
    f1=open(name,'r')
    print(f1.read())
    print()
