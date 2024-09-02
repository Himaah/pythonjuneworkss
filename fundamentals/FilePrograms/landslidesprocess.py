f=open("C:\\Users\\user\\Desktop\\PythonJuneWorks\\fundamentals\\FilePrograms\\landslides.txt","r")
data=[]
for line in f:
    lst=line.rstrip("\n").split(" ")
    dict={"state":lst[0],"year":lst[1],"death_count":int(lst[2])}
    data.append(dict)
# print(data)

# death per state

state_summary={}
for dict in data:
    state=dict.get("state")
    death_count=dict.get("death_count")
    if state in state_summary:
        state_summary[state]+=death_count
    else:
        state_summary[state]=death_count
print(state_summary)    







