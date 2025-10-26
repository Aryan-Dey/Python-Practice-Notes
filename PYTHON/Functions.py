# Creating a function
# syntax - def func_name():

def average(): # User Defined Function Defination
    a = int(input("Enter the no. - "))
    b = int(input("Enter the no. - "))
    c = int(input("Enter the no. - "))

    avg = (a+b+c)/3
    print(avg)

average()  # 1 Function Call
average()  # 2nd Function Call
average()  # 3rd Function Call


# Function With Arguments
def greet(name , end):
    print(f"Have a Good Day ! {name}  \n{end}")

greet("Aryan" , "Thank You")

# Return Type
def greet(name , end):
    print("Have a Good Day ! "+ name + " " + end)  #String Contatenation
    return "Done"

a = greet("Aryan" , "Thank You")
print(a)

# # Default Parameter Value
def greet(name , end = "Thank U"): # Agar Value provide ki hai toh voh use karega nahi toh default value
    print(f"Have a Good Day ! {name}  \n{end}")

greet("Aryan" , "Thanks")   
greet("Rohan")



# # Recursion
def fib(n):
    if( n == 0 or n == 1):
        return 1
    
    return n * fib(n-1)

n = int(input("Enter the no. - "))
print(f"The factorial of {n} is {fib(n)}")



