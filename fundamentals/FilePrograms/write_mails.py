emails= ["hima@gmail.com","abin@gmail.com"]

f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\emails.txt","w")
for email in emails:
    f.write(email+"\n")