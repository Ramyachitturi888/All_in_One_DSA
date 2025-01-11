from collections import defaultdict


# creating
my_dict={1:0,2:1,3:2}
my_dict1=defaultdict(list)

parent=[1,2,3,4]
child=[[1,2],[1],[3,4,5,6],[4,5,6,6]]

#Accessing Elements
print(my_dict.get(5)) # this will return None if item is not present
print(my_dict[3]) # it will throw an exception if not present

# Adding/Updating Elements
my_dict[4]=3
print(my_dict) # added if not present
my_dict[2]=2 # updated if present
print(my_dict)

#Removing Elements
remove_dict={1:0,2:1,3:2}
#1.pop()
my_dict.pop(2)
print(my_dict)

#2.del
del my_dict[1]
print(my_dict)
# popItem
my_dict.popitem()
print(my_dict)

#Iterating Through Dictionaries

for key in my_dict.keys():
    print(key, end="")
for value in my_dict.values():
    print("values ",value,end="")
for key,val in my_dict.items():
    print(key," : ",val)
"""DSA Applications
1 Counting Frequencies"""

arr = [1, 2, 2, 3, 3, 3]
freq={}
for i in arr:
    freq[i]=freq.get(i,0)+1
print(freq)

#Hash Map for Fast Lookup
nums = [2, 7, 11, 15]
target = 9

search={}
for i,num in enumerate(nums):
    complement=target-num
    if complement in search:
        print(search[complement],i)
        break
    search[num]=i

n=10
def fib(n,memo={}):
    if n<=1:
        return n
    if n not in memo:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
    return memo[n]
print(fib(n))
#Anagrams Grouping
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
anagrams=defaultdict(list)

for word in words:
    sorted_word=''.join(sorted(word))
    anagrams[sorted_word].append(word)
print(anagrams)





for i in range(len(parent)):
    my_dict1[parent[i]]=child[i]
print(my_dict1)

# getting items from dictionary
for key,val in my_dict.items():
    print("key ",key,"val ",val)

# flatten the dictionary
nested_dict = {"a": {"b": 1}, "c": {"d": 2}}
flatten =[key for outer,inner_dict in nested_dict.items() for key,val in inner_dict.items() ]
print(flatten)







