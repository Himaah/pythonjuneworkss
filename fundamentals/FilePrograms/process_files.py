f_read=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\years.txt","r")
f_noncent=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\noncentury.txt","w")
f_cent=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\century.txt","w")

for year in f_read:
    y=int(year.rstrip("\n"))
    if y%100==0:
        f_cent.write(str(y)+"\n")
    else:
        f_noncent.write(str(y)+"\n")