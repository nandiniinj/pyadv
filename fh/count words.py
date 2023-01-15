#count words in a file
fname=input("Enter the file name: ")  #enter the name with the extension

f= open(fname,"r")
data=f.read()

count=0
words=data.split()
print(words)

for w in words:
    if w in ['Me','me','myself','myself','my','My']:
        count=count+1

print("Count is: ",count)
f.close()
