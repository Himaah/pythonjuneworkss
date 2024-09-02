f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\news.txt","r")
# word_list=[]
# for line in  f:
#     word=line.rstrip("\n")
#     words=word.split(" ")
#     # print(words)

#     for w in words:
#         word_list.append(w)
# print(word_list)

word_list=[w for line in f for w in line.rstrip("\n").split(" ")]
word_count={w:word_list.count(w) for w in word_list}
# print(word_count)

def get_value(key):
    return word_count.get(key)
srt1=sorted(word_count,key=get_value,reverse=True)

# srt=sorted(word_count,key=lambda key:word_count.get(key),reverse=True)
print(srt1)