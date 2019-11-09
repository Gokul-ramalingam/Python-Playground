# Python Data Types
# Variables can hold values of different data types. Python is a dynamically typed language 
# hence we need not define the type of the variable while declaring it. The interpreter implicitly binds the value with its type.

# Python enables us to check the type of the variable used in the program. 
# Python provides us the type() function which returns the type of the variable passed.

a = 2
b = "Jhon"
c = 7.50

print(type(a))
print(type(b))
print(type(c))


# Python provides various standard data types that define the storage method on each of them. 
# The data types defined in Python are given below.

# Numbers
# String
# List
# Tuple
# Dictionary

# Number stores numeric values. Python creates Number objects when a number is assigned to a variable. For example

# Python supports 4 types of numeric data.

# int (signed integers like 10, 2, 29, etc.)
# long (long integers used for a higher range of values like 908090800L, -0x1929292L, etc.)
# float (float is used to store floating point numbers like 1.9, 9.902, 15.2, etc.)
# complex (complex numbers like 2.14j, 2.0 + 2.3j, etc.)


# Python allows us to use a lower-case L to be used with long integers.
#  However, we must always use an upper-case L to avoid confusion.
# A complex number contains an ordered pair, i.e., x + iy where x and y denote the real and imaginary parts respectively).



a = 3
b = 5  #a and b are number objects  


# String
# The string can be defined as the sequence of characters represented in the quotation marks. 
# In python, we can use single, double, or triple quotes to define a string.

# String handling in python is a straightforward task since there are various inbuilt functions and operators provided.
# In the case of string handling, the operator + is used to concatenate two strings as the operation "hello"+" python" 
# returns "hello python".
# The operator * is known as repetition operator as the operation "Python " *2 returns "Python Python ".

str1 = "hello python"
str2 = "Happy to learn you"

print(str1[0 : 2])   #printing first two character using slice operator  
print(str1[4])  #printing 4th character of the string
print(str1*2) #printing the string twice  
print(str1 + str2) #printing the concatenation of str1 and str2

# List
# Lists are similar to arrays in C. However; the list can contain data of different types. 
# The items stored in the list are separated with a comma (,) and enclosed within square brackets [].
# We can use slice [:] operators to access the data of the list. 
# The concatenation operator (+) and repetition operator (*) works with the list in the same way as they were working with the strings.

list = [1,"hello","python",2]

print(list)  #prints the entire list
print(list[3:]) #prints all the items after 3rd position
print(list[0:2]) #printing first two list items using slice operator in a single list
print(list + list) #printing the concatenation of two lists as a single list
print(list*3) #printing the list thrice as a single list
