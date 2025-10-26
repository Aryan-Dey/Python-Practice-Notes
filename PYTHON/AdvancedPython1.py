# # Walrus Operator (:=) ->
# if(n := len([1,2,3,4,5])) > 3: # List Contains more than 3 elements so if statement returns true and prints
#     print(f"List is to long {n} elements , expected <= 3") 
    

# # Variable Type Hints
# age : int = 25  # Bolta hai ki age ek int type ka input lega

# # Function Type Hints
# def greeting(name : str) -> str:  # Yaha pe function ek string type return karega (->) & input hai voh bhi string type hai(:)
#     return f"Hello , {name} !"
    
# print(greeting("Alice"))


# # Advanced Type Hints 

# from typing import List, Tuple, Dict, Union

# # List of Integers
# numbers : List[int] = [1,2,3,4,5] # Here, numbers in a Variable containing List of int type
# print(numbers)

# # Tuple of a string & an Integer
# person : Tuple[str , int] = ("Alice" , 30)
# print(person)


# # Dictionary with string keys and Integer values
# scores : Dict[str , int] = {"Alice" : 30 , "Bob" : 45}
# print(scores)

# # Union type for variables that can hold multiple types - input can be either str, int, float, etc
# identifier : Union[int , str] = "ID123"
# # identifier = 12345
# print(identifier)


# # Match case -> exactly as switch case
# def https_status(status):
#     match status:
#         case 200:
#             return "OK"
        
#         case 404:
#             return "Page Not Found"
        
#         case 500:
#             return "Internal Server Error"
        
#         case _:  # agar above given nos. kai alawa hum koi aur no. input dete hai toh yeh statement execute ho jayega
#             return "Unknown Status"

# print(https_status(200))
# print(https_status(404))
# print(https_status(500))
# print(https_status(5008))


# # Dictionary Merge & Update Operators
# dict1 = {'a' : 1 , 'b' : 2}
# dict2 = {'c' : 3 , 'd' : 4}
# merged = dict1 | dict2
# print(merged) # Dono Dictionary Merge ho jayegi


# # with statement -> can be used to perform operations on two or more files together
# with(
#     open("file1.txt") as f1,
#     open("file2.txt") as f2
# ):
#     # Code for processing files


# # Exception Handling
# try:
#     a = int(input("Enter your number: "))

# except Exception as e:  # When Exception case occurs still code executes without program interruption
#     print(e) 
     
# print("Enter a valid number !")


# # Raise Exception -> we can create custom Exceptions using raise keyword

# a = int(input("Enter 1st no. : "))
# b = int(input("Enter 2nd no. : "))

# if(b == 0):
#     raise ZeroDivisionError("You cannot set the denominator as 0")  # Created a custom error message
    
# else:
#     print(f"The division of above input is {a/b}")


# # try with else clause -> else statement will execute only when try code was successful
# try:
#     a = int(input("Enter your number: "))

# except Exception as e:  # When Exception case occurs still code executes without program interruption
#     print(e)
#     print("Enter a valid number !")
    
# else:
#     print("Else Executed Successfully")


# # try with Finally clause -> finally statement executes irrespective of whether exception occured or not 
# def main(): # finally clause useful within main statement
#     try:
#         a = int(input("Enter your number: "))

#     except Exception as e:  # When Exception case occurs still code executes without program interruption
#         print(e)
#         print("Enter a valid number !")
    
#     finally:
#         print("finally Executed Successfully")

# main()


# # global -> used to modify the variables outside the current scope

# a = 89

# def func():
#     global a 
#     a = 3
#     print(a)

# print(a)   # will print 89 as func not Executed 
# func()
# print(a)  # will print 89 if "a" inside finc is not declared global otherwise it will print 3


# # Enumerate Function -> adds a counter to an iterable and returns it
# l = [4,8,1,74,3]

# index = 0
# for item in l:
#     print(f"The {item} is at {index} index")
#     index += 1

# # Now using Enumerate Function
# for index , item in enumerate(l):
#     print(f"The {item} is at {index} index")  # Gives the same output as above


# # List Comprehensions -> Elegant way to create lists based on existing lists
# mylist = [1,5,7,2,6]

# squaredList = []
# for i in mylist:
#     squaredList.append(i*i)

# print(squaredList)


# #Now using List Comprehension
# squaredList = [i*i for i in mylist]

# print(squaredList) # Same o/p as above