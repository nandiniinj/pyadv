#zipping file

from zipfile import *

f=ZipFile("files.zip","w",ZIP_DEFLATED)
f.write("abcd.txt")
f.write("apps.txt")
f.write("message.txt")
f.close()
print("files.zip created successfully")
