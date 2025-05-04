class Student:

    name = None
    roll = None
    mob = None
    def __init__(self, *args):

        print(self)

        if(len(args)==0):
        
            print("zero args called")

        elif(len(args)==3):
            print("3 parameterized const")
            self.name = args[0]
            self.roll = args[1]
            self.mob = args[2]
    
    def display(self):
        print(type(self))
        print(self)
        print(self.name)
        print(self.roll)
        print(self.mob)


print("First Object ************************************************************8")
student1 = Student()

print("Second object************************************************************8")
student2 = Student("manideep",254,23980458435)

student3 = Student("manideep",254,23980458435)


st = {student1,student2,student3}

print(st)