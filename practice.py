#class for the student information to be maintained
class student_class:
    def __init__(self,srollno,sname,semail,sphone):
        self.srollno=srollno
        self.sname=sname
        self.semail=semail
        self.sphone=sphone
    def student_welcome(self):
        print("student welcome message")
    def stu_update(self):
        print("this is update method")
    def stu_delete(self):
        print("delete method")
#object creation for the class
obj=student_class(501,"anu","anu12@gmail.com",9908133590)
obj2=student_class(502,"bhanu","bhanu@gmail.com",9704122555)
#print details of students
print("student 1 details\n",obj.__dict__)
print("student2 details\n",obj2.__dict__)
#NOTE : if u have one class,, any number of objects can be created
obj.student_welcome()
obj.stu_update()
obj.stu_delete()

#write a program using class and object concept to maintan
#an employee information