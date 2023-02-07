class Test:
    count=0
    def __init__(self):
        Test.count+=1

    @classmethod
    def noOfObjects(cls):
        print("The number of objects created for test are: ",Test.count)

t1=Test()
t2=Test()
Test.noOfObjects()
t3=Test()
t4=Test()
t5=Test()
Test.noOfObjects()

#whenever the object is created the constructor runs
