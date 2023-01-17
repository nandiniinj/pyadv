#creating student.dat

import pickle  #for binary files
def createfile():
    f=open ("student.dat","ab")
    for i in range (3):
        sid=int(input("Enter the student id: "))
        name=input("Enter the name of the student: ")
        marks=int(input("Enter the student's marks: "))
        record=[sid,name,marks]
        pickle.dump(record,f)
        print("Record added to the file successfully")
    f.close()

#reading data from the file
    
def display():
    f=open("student.dat","rb")
    print("content of file is: ")
    try:
        while True:
            record=pickle.load(f)
            print(record)
    except:
        f.close()

createfile()
display()

    
