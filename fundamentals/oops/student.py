class Student:

    
    def __init__(self,roll_no,name,gender,course,adress):

        self.rollnum=roll_no
        self.name=name
        self.gender=gender
        self.course=course
        self.adress=adress

    def display_student(self):
        print(self.rollnum,self.name,self.gender,self.course,self.adress)

    def __str__(self):
        return self.name
        

# create objects

student_instance=Student(12,"saniya","female","python django","liya pg")
# student_instance.display_student()
print(student_instance)
