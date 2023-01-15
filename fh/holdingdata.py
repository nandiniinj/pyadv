#creating files to hold some data

f=open("apps.txt","w") #write mode

f.write("Facebook \n")
f.write("Instagram \n")
f.close()


f=open("apps.txt", "a") #append mode

f.write("Whatsapp \n")
f.write("Kindle \n")
f.close()


