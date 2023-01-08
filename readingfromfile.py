#reading data from the file in the output window

filename=input("Enter the file name: ") #taking the filename from the user (type the filename including the extension (ex: apps.txt))

f=open(filename, "r")
data=f.read()
print(type(data))#printing the type of the data
print(data)
f.close()
