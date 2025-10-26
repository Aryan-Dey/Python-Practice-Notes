# # Q1)

# class programmer():
    
#     def __init__(self , name, language, salary, dept):
#         self.name = name
#         self.language = language
#         self.salary = salary
#         self.dept = dept
        
#     def getinfo(self):
#         print(f"Name is {self.name} who codes in {self.language} having a salary of {self.salary} & works in dept. {self.dept}")
        

# a = programmer("Harry", "Python",120000, "Technical")
# a.getinfo()
# b = programmer("Aryan", "Data Scientist",500000, "Upper Management")
# b.getinfo()
# c = programmer("Vishal", "JavaScript",220000, "Web DEV")
# c.getinfo()
# d = programmer("Prem", "C++",20000, "Kaam Wala")
# d.getinfo()

# #Q2)
# class Calculator():
    
#     def __init__(self , n):
#         self.n = n
        
#     def square(self):
#         print(f"The square of {self.n} is {self.n*self.n}")
    
#     def cube(self):
#         print(f"The cube of {self.n} is {self.n*self.n*self.n}")
        
#     def squareroot(self):
#         print(f"The square of {self.n} is {self.n**1/2}")
    

# a = Calculator(4)
# a.square()
# a.cube()
# a.squareroot()

# # Q3)
# class Demo():
#     a = 4
    
# o = Demo()
# print(o.a)  # Prints Class attribute as instance attribute is not set
# o.a = 0
# print(o.a) # Print the instance attribute
# print(Demo.a)  # Class attribute does not change