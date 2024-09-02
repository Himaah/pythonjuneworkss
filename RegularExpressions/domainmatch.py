from re import fullmatch

f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\RegularExpressions\\domain.txt")
pattern="[\\w\\W]+\\.com"      #meaning is .com so \\.
for line in f:
    domain=line.rstrip("\n")
    matcher=fullmatch(pattern,domain)
    if matcher !=None:
        print(domain)


