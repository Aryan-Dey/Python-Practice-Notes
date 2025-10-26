class Employee:
    language = "Py"   # This is an class attribute
    salary = 1200000
    
    @staticmethod  #Sometimes we need a function that does not use the self-parameter. usable only when no attribute is passed
    def greet():
        print("Good Morning") 
    
    def getinfo(self):
        print(f"The language is {self.language} & salary is {self.salary}.")

harry = Employee() # This is an Object/Instance Attribute
harry.name = "Harry" 
harry.language = "JavaScript"  #Instance Attributes take preference over class attributes during assignment & retrieval
print(harry.name , harry.language, harry.salary)

# harry.greet()  This will give error as it will pass harry as an argument. equivalent to Employee.greet(harry). 
harry.getinfo()

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name , rohan.salary, rohan.language)
rohan.greet() #Marked as static method



# Initialising using Constructor
class Employee:
    
    def __init__(self , name , language, salary):  #dundar method (Constructor) - Automatically called
        self.name = name
        self.language = language
        self.salary = salary
    
    @staticmethod  #Sometimes we need a function that does not use the self-parameter. usable only when no attribute is passed
    def greet():
        print("Good Morning") 
    
    def getinfo(self):
        print(f"The language is {self.language} & salary is {self.salary}.")

harry = Employee("Harry" , "JavaScript", 1200000) # This is an Object/Instance Attribute
print(harry.name , harry.language, harry.salary)

# harry.greet()  This will give error as it will pass harry as an argument. equivalent to Employee.greet(harry). 
harry.getinfo()