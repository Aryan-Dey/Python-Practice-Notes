# Lists - A built in data type that can store a set of values ,concept somewhat similar to Arrays
# It can store elements of different types (int,float,str,etc) on the same list
# String is Immutable(value cannot change) in python whereas list is Mutable(Values can change)

str = "Yes"
print(str[0])
str[0] = "y"  #Here, we cannot change the value will show error 
print(str)

str = ["Hello"] #Declaring a List
print(str[0])
str[0] = "NO"   #Here, value changed but no error
print(str[0])


marks = [84,219,384,4952,329]
print(marks)
print(marks[3])
print(type(marks))


marks = ["Arjun",95 , "Pass"]
print(marks)
print(marks[0])
print(marks[2])
print(len(marks))   #Prints the length of list


#List Slicing - Similar to String slicing 
#Syntax- list_name = [starting_index : Ending_index]    Ending index is not included
marks = [91,382,44,32,64,21]
print(marks[1:5])
print(marks[:5])
print(marks[1:])
print(marks[-5:-1])


# some List Keywords

list = [2,1,3]

list.append(4)  #inserts the element at the last
print(list)

list.sort()  #Sorts the list in ascending order (Default)
print(list)

list.sort(reverse = True)  #Sorts the list in descending order , Can sort strings also based on their First letter
print(list)

list.insert(1 , 5)   #Insert element 5 at index 1
print(list)

list.reverse()  #Reverses the list
print(list)

print(list.append(7))  #None show karega but operate karega , VALID for every keyword here
print(list)

list.remove(3)  #Removes 3 from the list as soon as it occurs
print(list)

list.pop(4)  #Removes the last element present at 4th index
print(list)

L = ['Micheal Jackson',10.2]
print(L)
L.extend(['pop',10]) #Does exactly what append does but for more than 1 element (ek time pe 2 or more elements insert)
print(L)



# Tuple - A built in Data Types tha allows us to create Immutable Squences of values
tup = (1,2,4,5)
print(tup)
print(type(tup))
print(tup[1])
print(tup[1:3])

tup = ()  #Valid Empty Tuple
print(tup)
tup[0] = 5  # This is not possible

tup = (1) # Int recognise karega not tuple , similar for string
print (type(tup)) 
tup = (1,) # Yeh tuple recognise karega

#TUPLE Methods
tup = (2,1,3,1)
print(tup.index(2)) # 2 here is the element & it will return index at which 2 is placed 
print(tup.count(1)) # returns no. of times 1 has occurred


#Q) WAP to ask the user to enter names of their 3 fav. movies & store them in a list
movies = []
movies.append(input("Enter 1st movie"))
movies.append(input("Enter 2nd movie"))
movies.append(input("Enter 3rd movie"))
print(movies)


#Q) WAP to check if a list is plaidrome of elements
list = [1,2,1]
copyls = list.copy()
copyls.reverse()

if(copyls == list):
    print("Palindrome")
else:
    print("Not plaindrome")


# Tuple Operations
# Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4)

# Membership Testing - Find particular element in Tuple
my_tuple = (1, 2, 3)
print(2 in my_tuple)  # Output: True
print(5 in my_tuple)  # Output: False

# Length of Tuple 
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3


# Nested List - It's a list that contains other lists as its elements
# Allows organizing data in a Hierarchical and Multi-Dimensional Structure
nested_list = [[1,2],[3,4],[5,6]]
print(nested_list[1])  #Accessing Sub-Lists
print(nested_list[1][0]) # Accessing individual Elements
nested_list[0] = [7,8]  #Modifying Sub-List
print(nested_list)
nested_list[0][1] = [9] #Modifying Individual Element
print(nested_list)

# Sorting a Tuple
genres_tuple=(3,1,43,4,54,24)
sorted_tuple = sorted(genres_tuple)
print(sorted_tuple)

# Sum in Tuple
numbers = (10, 20, 5, 30)
print(sum(numbers)) #Sums up the elements in Tuple provided they are int or float
