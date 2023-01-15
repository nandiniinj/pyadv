import csv

with open ("employee.csv","w", newline="") as f:
    w=csv.writer(f) #returns csv writer object
    w.writerow(["ENO", "ENAME", "ESAL","EADD"])
    n=int(input("Enter no of employees: "))
    for i in range (n):
        eno=input("Enter employee no.: ")
        ename=input("Enter employee name: ")
        esal=input("Enter employee salary: ")
        eadd=input("Enter employee address: ")
        w.writerow([eno,ename,esal,eadd])
    print ("Total employee data written to csv file successfully ")

    f=open("employee.csv","r")
    r=csv.reader(f)
    for record in r:
        print(record)
    f.close()
           
    
