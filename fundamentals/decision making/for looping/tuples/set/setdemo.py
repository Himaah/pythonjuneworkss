# sets
# ===

name={"hima","gouri"}
s=set()     #empty set

# duplicates are not allowed
# insertion order is not preserved
# no elements cannot be fetched from the sets using index positioning
# no index position
# mutable


# name.add("kochi") #to add an element
# print(name)

# name.clear() #to remove all elements from the set
# print(name)

# name.pop()  #to remove a random set object
# print(name)

# name.discard("hima") #to remove an element if it is in the set
# print(name)


names1={"hima","gouri"}
names2={"swathi","gouri"}
# names1.update(names2)  #add elements from any collection to the set
# print(names1)


#union()  intersection()   difference()


union=names1.union(names2)  #return a new set with two  sets combined
print(union)   

intersection=names1.intersection(names2)  #to return tht common element and return it as a new set
print(intersection)

diff=names1.difference(names2) #return elements from the first set which is not in second set
print(diff)

symdiff= names1.symmetric_difference(names2)  #combine all elements from two sets but excluding the common elements
print(symdiff)

