# Advanced Python 1- 
# # Q1)
# try:
#     with open("1.txt" , "r") as f1:
#         print(f1.read())
         
# except Exception as e:
#     print(e)
    
# try:
#     with open("2.txt" , "r") as f1:
#         print(f1.read())
         
# except Exception as e:
#     print(e)
    
# try:
#     with open("3.txt" , "r") as f1:
#         print(f1.read())
         
# except Exception as e:
#     print(e)
    
# print("Thank You")

# # Q2)
# l = [1,2,3,4,5,6,7,8]

# for i,item in enumerate(l):
#     if i == 2 or i == 4 or i == 6:
#         print(item)


# # Q3)
# n = int(input("Enter Your number: "))

# table = [n*i for i in range(1,11)]
# print(table)
    

# # Q4)
# # Method 1 -
# a = int(input("Enter Your number: "))
# b = int(input("Enter Your number: "))

# if(b == 0):
#     raise ZeroDivisionError("You can't place denominator as 0")
# else:
#     print(a/b)
    
# # Method 2 - 
# try:
#     a = int(input("Enter Your number: "))
#     b = int(input("Enter Your number: "))
#     print(a/b)

# except ZeroDivisionError as v:
#     print("Infinite")

