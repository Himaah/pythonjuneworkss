vehicle_numbers=["KL123","KL1234","KL345"]
f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\vehiclenumbers.txt","w")
for num in vehicle_numbers:
    f.write(num+"\n")