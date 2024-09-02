from json import load

f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\JsonWorks\\films.json")

movies= load(f)

# print(movies)

for  mov in movies:
    print(mov.get("title"))