# Look Into Virtual Environment 

# Lambda Function - Function created using an expression 

#Normal Function
# def sqaure(n):
#     return n*n
# print(sqaure(5))

#Now using Lambda Function
# square = lambda x: x*x
# print(square(5))

# sum = lambda a,b,c: a+b+c
# print(sum(4,6,10))


# # Join Function - Creates a string from iterable objects
# list = ["apple", "mango","Banana" ]
# result = " and ".join(list)
# ans = " Kuch bhi daal sakte hai ".join(list)

# print(result)
# print(ans)

# # Format Function - Formats the values inside the string into a desired output (Rarely used)
# a = "{} is a good {}".format("Harry", "Boy")
# b = "{1} is a good {0}".format("Harry", "Boy")

# print(a)
# print(b)


# # Map Function- Map applies to a function to all the items in an input list
# l = [1,2,3,4,5]
# square = lambda x:x*x
# sqlist = map(square, l)
# print(list(sqlist))


# # Filter Function- Creates a list of items for which the function returns true
# l = [1,2,3,4,5]

# def even(n):
#     if(n % 2 == 0):
#         return True
#     return False

# onlyEven = filter(even , l)
# print(list(onlyEven))


# Reduce Function - Reduce applies a rolling computation to sequential pair of elements
from functools import reduce
l = [1,2,3,4,5]

def sum(a,b):
    return a+b

print(reduce(sum , l)) # Sum return kardega list ka