print("My name is Aryan") 
print("Lagi padhi hai") 
print("My name is Aryan","Lagi padhi hai") 
print(23+58)


name = "Aryan" #String can also be defined in ' ' or " " or "' '" 
age = 20 
old = False 
a = None #Same as NULL 
print("My name is : ", name , "& my age is ", age) 
print(type(name)) 
print(type(age)) 
print(type(old)) 
print(type(a)) 

# Python is a case Sensitive lang. matlab A & a different hai 
# Punctuators - Symbols to oraganise sentence structure in programming. Egs-() , {}, [], @, -=,+=, *=, etc 
# Python is Implicit Lang. matlab usmai hume batana nahi padhta ki int,str,float variable hai.C++ is Explicit Lang. 
# Python is an INDENTATION Lang. matlab proper spacing deni padhti hai like if else wale mai 

#Expression Executuion 

# i) String and Numeric Values can operate together with * 
A,B = 2,3 
Txt = "a" 
print(A*Txt*B)  #O/p- aaaaaa 


# ii) String and String Values can operate together with + also known as Concatenation 
A , B = "2" , 3
Txt = "a" 
print((A+Txt)*B) #O/p - 2a2a2a 
print((A+B)*Txt) #o/p - Error 


# iii) Numeric Values can operate with all Arithmatic Operators (Follows Arithmatic Precedence Order) 
A, B, C = 3, 4, 5 
print(A+B*C) #o/p - 23


# iv) Arithmatic Operation with Int and Float will result in Float 
A , B = 5 , 10.0 
print(A+B) #o/p - 15.0 


# v) Division of 2 int will give us Float 
A,B = 1,2 
print(A/B) #o/p - 0.5 


# vi) Interger Division (//) with float and int will give int but displayed as float 
A,B = 1.5 , 3 
print(A//B , A/B) #o/p - A//B = 0.0(Int. o/p) & A/B = 0.5 


# vii) Remainder is -ve when Denominator is -ve. If Numerator is -ve then will get +ve Remainder 
A,B = -5,2 
C,D = 5,-2 
E = A%B 
F = C%D 
print(E , F) #o/p - E=1 , F= -1


# input()- Used to accept values from the user. Similar to cin>> 
name = input("Name : ") 
age = int(input("Age: ")) #Int type input lega. Similar for different Data types 
print("My name is",name , "& my age is",age) 



# Conditional Statement (if-elif-else (syntax)) Not necessary it can seperate if or if-elif also 


x = int(input("Enter No. - "))
if(x % 5 == 0):
    print("Multiple of 5 ")
else:
    print("Not multiple of 5 ")



light = input("Colour: ") 
if(light == "red"): 
    print("STOP") 
elif(light == "yellow"): 
    print("Look") 
elif(light == "green"): 
    print("GO") 
else: 
    print("Light is Broken") 



marks = int(input("Marks : ")) 
if(marks >= 90): 
    print("A") 
elif(marks >= 80 and marks < 90): 
    print("B") 
elif(marks >= 70 and marks < 80): 
    print("C") 
else: 
    print("D") 


#Conditional Statements in single line (Ternary Operator) 
# Syntax using 2 variables - <var> = <val1> if <Condition> else<val2> 
food = input("food : ") 
eat = "Yes" if food == "cake" else "NO" 
print(eat) 


# Syntax using 2 statements- <stt1> if<Condition> else<stt2> 
food = input("Food : ") 
print("Sweet") if food == "cake" or food == "Jalebi" else print("Not Sweet") 


# Syntax for True and False - <var> = (False_Val , True_Val) [<Condition>] 
age = int(input("Age: "))
vote = ("can vote" , "cannot vote") [age < 18] 
print(vote)


