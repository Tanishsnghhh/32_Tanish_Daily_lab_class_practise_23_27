
#btech pgdm
class Student:

    count = 0 
    
    n=input("enter name")
    a=input("enter age")
    d=input("enter department")
    if d.upper()=="BTECH":
        print("BTECH DEPARTMENT")
    elif d.upper()=="PGDM" :
        print("PGDM")
    else :
        print("plese enter btech or pgdm")

 

    ask =input("enter you want more students (yes,no):")
    while True !="no":

        n=input("enter name")
        a=input("enter age")
        d=input("enter department")
        if d.upper()=="BTECH":
         print("BTECH DEPARTMENT")
        elif d.upper()=="PGDM" :
           print("PGDM")
        else :
            print("plese enter btech or pgdm")
        ask =input("enter you want more students (yes,no):")



    def __init__(self):

        n=input("enter name")
        a=input("enter age")
        d=input("enter department")
        if d.upper()=="BTECH":
            print("BTECH DEPARTMENT")
        elif d.upper()=="PGDM" :
             print("PGDM")
        else :
            print("plese enter btech or pgdm")

 

    ask =input("enter you want more students (yes,no):")
    while ask !="no":
        
        n=input("enter name")
        a=input("enter age")
        d=input("enter department")
        if d.upper()=="BTECH":
         print("BTECH DEPARTMENT")
        elif d.upper()=="PGDM" :
           print("PGDM")
        else :
            print("plese enter btech or pgdm")
        ask =input("enter you want more students (yes,no):")


        self.name=n
        self.age=a
        self.department=d
        print("constructor is called")
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("department:",self.department)
        
        Student.count=Student.count+1
      
obj=Student("ABC",18)
obj.display()
obj1=Student("xyz",30)
obj1.display()
obj2=Student()
print(Student.count)




class ITM:
    
    Allstudentkadata = []
    btechcount=0
    pgdmcount=0
    def getdata(self):
        while True:
            name = input("Enter the student's name: ")
            age = int(input("Enter the student's age: "))
            address = input("Enter the address: ")
            department = input("Enter the department (btech/pgdm): ")
            if department.lower() == 'btech':
                ITM.btechcount+=1
                ITM.Allstudentkadata.append({'Name': name, 'Age': age, 'Address': address, 'Department': 'BTech'})
            elif department.lower() == 'pgdm':
                ITM.pgdmcount+=1
                ITM.Allstudentkadata.append({'Name': name, 'Age': age, 'Address': address, 'Department': 'PGDM'})

            ask = input("Do you want to add more students? (yes/no): ")
            if ask.lower() != 'yes':
                break

    def display_list(self):
        print("List of Student Information:")
        for student in ITM.Allstudentkadata:
            print(student)

obj1 = ITM()
obj1.getdata()
obj1.display_list()
print("Number of students in btech:-",ITM.btechcount)
print("Number of students in pgdm:-",ITM.pgdmcount)
print("Total number of students in ITM SKILLS UNIVERSITY:-",ITM.btechcount+ITM.pgdmcount)





