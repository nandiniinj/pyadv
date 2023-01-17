#myfile=open(r'D:\AnupaCC\Python\filehandling\apps.txt','r')

myfile=open('apps.txt','r')

print("The content of file is :")
print(myfile.tell())
data=myfile.read()
print(data)
print(myfile.tell())

myfile.seek(5)
print(myfile.tell())
s=myfile.read(3)
print(s)
print(myfile.tell())
myfile.close()
