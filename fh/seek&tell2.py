'''here we are seeking the cursor to move to a particular position.'''

#we can use seek() method to move cursor(file pointer) where we want.
#by default file pointer is at the start when you open the file.
#after reading the file the pointer moves to the end.


data="All students are STARS"
f=open ("abcd.txt","w")
f.write(data)
f.close()

with open ("abcd.txt","r+") as f:
    #text=f.read()
    #print(text)
    print("The cursor position is currently at: ",f.tell())
    f.seek(17)
    print("Now the cursor position is at: ",f.tell())
    f.write("GEMS!!!")
    f.seek(0)
    text=f.read()
    print("Data after modification: ")
    print(text)
