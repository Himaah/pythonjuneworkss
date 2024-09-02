#dictionaries
#collection of elements as a key value pair
# dict={key:value}

# student={"name":"gouri","course":"fullstack"}
# print(student["name"])

# print(student.keys())
# student["name"]="hima"

# student["place"]="kollam"
# print(student)

# itemss=student.items()   #key values are arrabged in tuples and enclosed in lists
# print(itemss)


# student={"name":"sukumar", "course":"fullstack","course":"datascience"}
# print(student)
#** KEY SHOULD BE UNIQUE !!!! OTHERWISE LAST VALUE IS TAKEN !!! **

student={"name":"sukumar", "course":"fullstack","place":"kochi"}
# for i in student:
#     # print(student[i])
#     print(f"{i}={student[i]}")


#update the value of course as datascience through iteration

# for i in student:
#     if i=="course":
#       student[i]="datascience"

# print(student)

# delete a key "place" if it is present in the dict using iteration
#FOR DELETION student.pop("place")   - METHOD
student={"name":"sukumar", "course":"fullstack","place":"kochi"}
# for i in student:
#    if i == "place":
#     student.pop(i)
# print(student)
# student={"name":"sukumar", "course":"fullstack","place":"kochi"}

student={"name":"sukumar", "course":"fullstack","place":"kochi"}
for i in list(student.keys()):  # Create a list of keys to iterate over
    if i == "place":
        student.pop(i)
print(student)
