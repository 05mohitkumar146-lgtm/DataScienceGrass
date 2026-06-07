# Student record System 
class Student:
    def __init__(self,id,name,branch,cgpa):
        self.name=name
        self.id=id
        self.branch=branch
        self.cgpa=cgpa
    def display(self):
        print(f"ID:-{self.id}")
        print(f"Name:-{self.name}")
        print(f"Branch:-{self.branch}")
        print(f"CGPA:-{self.cgpa}")

class StudentManager:
    def __init__(self):
        self.students=[]
    def addStudent(self):
        id=int(input("enter your id:-"))
        name=input("enter your name:-")
        branch=input("enter your branch:-")
        cgpa=float(input("enter your cgpa:-"))
        student=Student(id,name,branch,cgpa)
        self.students.append(student)
        print("Student added successfully")
    def display(self):
        if not self.students:
            print("no student record")
        else:
            for i in self.students:
                i.display()

    def search(self):
        temp=int(input("enter ID:-"))
        for i in self.students:
            if i.id==temp:
                i.display()
                return
        print("student not found")
    def update(self):
        self.temp=int(input("enter the ID:-"))
        for i in self.students:
            if i.id==self.temp:
                i.name=input("enter the new name:-")
                i.id=int(input("enter the ID:-"))
                i.branch=input("enter the branch:-")
                i.cgpa=input("enter the cgpa:-")
                print("updation is successfully done")
                return
        print("record not found")
    def deletion(self):
        temp=int(input("enter the ID:-"))
        for i in self.students:
            if i.id==temp:
                self.students.remove(i)
                print("deletion is successfullt done")
                return
        print("record not found")

management=StudentManager()
while True:
    print("=====Welcome to student record system=====")
    print("1.Add student")
    print("2.Update student")
    print("3.Delete student")
    print("4.search student")
    print("5.display all student")
    print("6.exit")
    choice=int(input("enter your choice:-"))
    if choice==1:
        management.addStudent()
    elif choice==2:
        management.update()
    elif choice==3:
        management.deletion()
    elif choice==4:
        management.search()
    elif choice==5:
        management.display()
    elif choice==6:
        break 
    else:
        print("Invalid choice please try to choose option from the above mention points")
