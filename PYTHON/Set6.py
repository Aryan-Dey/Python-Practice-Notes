# Conditional Expressions
#  Q1)
a = int(input("Enter no. - "))
b = int(input("Enter no. - "))
c = int(input("Enter no. - "))
d = int(input("Enter no. - "))

if( a>b and a>c and a>d):
    print(a)
elif( b>a and b>c and b>d):
    print(b)
elif( c>a and c>b and c>d):
    print(c)
else:
    print(d)

# Q2)
maths = int(input("Enter math marks"))
physics = int(input("Enter physics marks"))
chemistry = int(input("Enter chemistry marks"))

avg = (maths + physics + chemistry)/3 

if(avg > 40 and maths > 33 and physics > 33 and chemistry > 33):
    print("Student Passed")

else:
    print("Student Failed")


# Q3)
# in- The in operator checks if a phrase is present in the email.
message = input("Enter your message - ")
p1 = "Make a lot of money"
p2 = "Buy Now"
p3 = "Subscribe this"
p4 = "Click This"


if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Spam")
else:
    print("Not Spam")

# Method 2
message = input("Enter your message - ")
phrases = ["Make a lot of money", "Buy Now", "Subscribe this", "Click This"]

if (phrases[0] in message or 
    phrases[1] in message or 
    phrases[2] in message or 
    phrases[3] in message):
    print("Spam")
else:
    print("Not Spam")


# Q4)
username = input("Enter Username -")

if(len(username) < 10):
    print("Less than 10")
else:
    print("More than 10")


# Q5)
name = input("Enter your name - ")
list = ["Aryan" , 'Dhruv', "Vishal", "Prem"]

if((list[0] in name) or (list[1] in name) or (list[2] in name) or (list[3] in name)):
    print("Name present")
else:
    print("Absent")


