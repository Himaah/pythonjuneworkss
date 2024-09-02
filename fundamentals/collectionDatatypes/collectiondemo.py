# colllection datatype
# list   tuple   set   dictionary

# to manage a group of objects
# defined as classes
# no size limit,no datatype specification


#  define      order_preserved     duplicates_alllowed    mutable     methods
# [],list()     yes                  yes                   yes         

#    1. lists 
#   ===========

lst=[10,]
lst=list()


mobile_name=["samsungA20","nokia","iphone13","vivo"]
print(mobile_name[3])

mobile_name[2]="redmi note8"
print(mobile_name)



colors=["red","blue","green","yellow","red","blue","green","yellow","red","blue","green","yellow"]


for i in range(0,len(colors)):

    print(colors[i])
