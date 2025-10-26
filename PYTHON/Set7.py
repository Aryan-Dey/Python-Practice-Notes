# For & While Loop-
# for loop in programming is a control structure that allows the repeated execution of a set of statements for each item in a sequence,
#  such as elements in a list or numbers in a range, enabling efficient iteration and automation of tasks
# Range(0,5) -> include karta hai - 0,1,2,3,4
# For loop mai auto-increment (++) by default hai whereas While loop mai nahi hai 
# Difference b/w For and While - 
# For loop certain no. of time hi chalega whereas while loop tab tak chalega jab tak condition false nahi ho jati
 
# # Q1)
n = int(input("Enter The no. - "))

i = 0
for i in range(1 , 11):  # Step_size(i++) = 1 (Default)
    print(f"{n} X {i} = {n * i}")


# # Q2)
l = ["Harry","Soham","Sachin","Rahul"]

for name in l:
    if(name.startswith("S")):
        print(name)

# # Q3)
n = int(input("Enter The no. - "))
i = 0

while(i < 11):
    print(f"{n} X {i} = {n * i}")
    i += 1

# # Q4)
n = int(input("Enter The no. - "))

for i in range (2 , n):
    if(n % i == 0):
        print("Not Prime")
        break

else:
    print("Prime")

# # Q5)
n = int(input("Enter The no. - "))
i = 0
sum = 0

while(i < n+1):
    sum += i
    i += 1

print(sum)  

# # Q6)
n = int(input("Enter The no. - "))
product = 1

for i in range (1,n+1):
    product *= i

print(product)


# Q7)
#    *    2 space hai
#   ***   1 space
#  *****  0  space

n = int(input("Enter The no. - "))

for i in range (1,n+1):
    print(" "*(n-i) , end = "")
    print("*"*(2*i - 1), end = "" )
    print("")

#     *
#   ***
# *****
n = int(input("Enter The no. - "))

for i in range (1,n+1):
    print("  "*(n-i) , end = "")  # Ek Extra Space add Karde idhar
    print("*"*(2*i - 1), end = "" )
    print("")


# # Q8)
# *
# **
# ***
n = int(input("Enter The no. - "))

for i in range(1 , n+1):
    print("*"*i , end ="")
    print("")

# # Q9)
# for n = 4
# ****
# *  *
# *  *
# ****
n = int(input("Enter the no. - "))

for i in range (1,n+1):
    if(i == 1 or i == n):
        print("*"*n , end="")
    else:
        print("*", end="")
        print(" "*(n-2) , end="" )
        print("*" , end ="")
    print("")


# # Q10) reverse miltipication
n = int(input("Enter the no. - "))

for i in range (1 , 11):
    print(f"{n} X {11-i} = {n*(11-i)}")



# The Enumerated For Loop
# Have you ever needed to keep track of both the item and its position in a list? An enumerated for loop comes to your rescue. 
# It's like having a personal assistant who not only hands you the item but also tells you where to find it.

# Consider this example:

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):#Enumerate func. acts as a counter for iterable (like list,tuple,strings) and returns it as an enumerate object 
    print(f"At position {index}, I found a {fruit}")


for i in range(-4,5):
    print(i)

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']

for Genre in Genres:
    print(Genre)