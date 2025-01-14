#Create a Set:

my_set=set()
my_set2={2,3,1,4}

#Adding and Removing Elements
my_set.add(1)
my_set.add(2)
my_set.remove(1)

print(my_set)


#discard(element): Removes an element (does nothing if not found).
my_set2.discard(5) #O(1)
my_set2.discard(3)
print(my_set2)

#	pop(): Removes and returns an arbitrary element.
print(my_set2.pop()) #O(1)

#Membership Check:

if 2 in my_set2: # O(1)
    print(True)

#	Length:

print(len(my_set2))


#Set Operations (Union, Intersection,Difference,Symmetric Difference

#1.union
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union ",set1|set2) #O(len(s1) + len(s2))
print("Intersection ", set1 & set2 ) # O(min(len(s1), len(s2)))
print("Difference ", set1-set2) #O(len(s1))
print(" Symmetric Difference ", set1^set2) #O(len(s1) + len(s2))

#Subset and Superset

print(set1.issubset(set2)) #O(len(s1))
print(set1.issuperset({1,2})) #O(len(s2))

#Disjoint
print(set1.isdisjoint({6,7}))

#Iterate Through a Set
for val in set1:
    print(val)

#Copy and Clear

new_set=set1.copy()
print(new_set)
new_set.clear()
print(new_set)

#A frozen set is an immutable version of a set.
frozen =frozenset([1,2,3,4])
print(frozen)


#DSA-Specific Use Cases
#1. Finding Unique Elements:

arr=[1,2,3,4,5,6,4,2]
print("unique values ",set(arr))

#Removing Duplicates from a String:
string = "aabbccz"
print("unique vals ","".join(set(string)))

#Set Intersection in Graph Algorithms:
graph1_neighbors = {1, 2, 3,4}
graph2_neighbors = {3, 4, 5}

common_neighbors= graph1_neighbors & graph2_neighbors
print("common neighbors ",common_neighbors )

#Checking for Subsets in Subarray Problems:
subset = {1, 2}
main_set = {1, 2, 3, 4}
print("is subarray ", subset.issubset(main_set))
