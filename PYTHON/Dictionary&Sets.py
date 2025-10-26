# Dictionary -> Collection of Key - Value pairs
# Keys have to be Unique and Immutable whereas Values can be mutable, duplicates, etc. 

d = {} # Empty Dictionary

marks = {
    "Harry" : 100,
    "Shubham": 56,
    "Aryan" : 100,
    "No.": [1,2,9]
}

print(marks , type(marks))
print(marks["Aryan"])
print(marks["No."]) 

# Dictionary Methods

print(marks.items())  #Returns a list of (Key , value) tuple
print(marks.keys())  # Returns all the keys of the tuple
print(marks.values()) # Returns all the values of the tuples
marks.update({"Harry" : 99 , "Sahiti " : 0} )  #Updates the dictionary if value doesn't exist it creates & adds at the last
print(marks)

print(marks.get("Aryan")) #Returns the value of the specified Key

print(marks.get("Aryan1"))  # Returns none if value doesn't exist
print(marks["Aryan1"])  # Returns an error

# # Some more methods 
# # copy() - Creates a shallow copy of the dictionary
my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()  
print(new_dict)  

# # fromkeys() - Creates a new dictionary with keys from an iterable and values set to a specified value (or None by default).
keys = ('a', 'b', 'c')
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# # pop(): Removes and returns the value for a specified key. If the key is not found, it returns a default value if provided; 
# # otherwise, it raises a KeyError.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.pop('b'))  # Output: 2
print(my_dict)  # Output: {'a': 1, 'c': 3}

# # popitem(): Removes and returns the last inserted key-value pair as a tuple. 
# # In Python 3.7+, dictionaries maintain insertion order.
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict.popitem())   #  Output: ('c', 3)
print(my_dict)   # Output: {'a': 1, 'b': 2}

# Deleting an entry from Dictionary
del(my_dict["a"])
print(my_dict)  



# Sets -> Collection of non-repetitve elements
s = {1,4,7,9,4,4,4} 
print(s) # 4 will only be printed once

a = set() # Empty set
b = {} # Empty Dictionary
print(type(a))
print(type(b))


# Operations on Sets
s = {1,8,2,3}

# Add into set
s.add(5)

#Len(s) - returns length of set
print(len(s))

# s.romove(element) - Updates the set and removes that element
a = (s.remove(2))
print(len(s))

# pop() - Removes an arbitary element from the set & return the element removed
s.pop()

# clear() - empties the set s
s.clear()

# Union() - Returns a new set with all items from both sets
s1 = {1,4,7,10,21}
s2 = {2,4,6,10,7,24}
print(s1.union(s2))

# Intersection - Returns a set which contains only items from both set
print(s1.intersection(s2))
s3 = s1 & s2 #Another expression of intersection function
print(s3)

# difference(): Returns a new set containing elements in the original set but not in the other set(s). 
# Equivalent to the - operator.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2))  # Output: {1}


#isdisjoint(): Returns True if the two sets have no elements in common.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

# issubset(): Returns True if set2 is a subset of set1
print(set1.issubset(set2))

 
