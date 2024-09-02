f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\students.txt","r")
students=[]
for stud in f:
    students.append(stud.rstrip("\n"))
print(students)