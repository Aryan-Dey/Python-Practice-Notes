# Functions & Recursion
# Help(function_name) to get info. how to use this function

# # Q1)
def greatest():
    a = int(input("Enter your no. - "))
    b = int(input("Enter your no. - "))
    c = int(input("Enter your no. - "))

    if(a > b and a > c):
        print(a)
    elif(b > a and b > c):
        print(b)
    else:
        print(c)

greatest()    


# # Q4)
def sum(n):
    if(n == 0):
        return 0
    
    return n + sum(n-1)

n = int(input("Enter your no. - "))
print(f"Sum of {n} digits is {sum(n)}")

# # Q5)
def pattern(n):
    for i in range (0, n+1):
        print("*"*(n-i) , end="")
        print("")

n = int(input("Enter your no. - "))
pattern(n)

# # Q6)
def conversion(n):
    return n * 12

n = int(input("Enter your no. - "))
print(f"{n} Inches = {conversion(n)} cms")

# Q8)
def table(n):
    for i in range (1, 11):
        print(f"{n} x {i} = {n*i}")
    
n = int(input("Enter your no. - "))
table(n)


# Write a function code to find total count of word little in the given string: 
# "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, 
# Mary went Everywhere that Mary went The lamb was sure to go"**

# Write your code below and press Shift+Enter to execute
def freq(string , passedkey):
    words = []
    words = string.lower().split()
    dict  ={}

    for key in words:
        if (key == passedkey):
            dict[key] = words.count(key)

    print(f"Total Count of {passedkey} in the string is {dict[passedkey]}")

freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb."
    "Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go","little")