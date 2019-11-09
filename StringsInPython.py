# Python String
# Till now, we have discussed numbers as the standard data types in python.

# In python, strings can be created by enclosing the character or the sequence of characters in the quotes.
#  Python allows us to use single quotes, double quotes, or triple quotes to create the string.

# Consider the following example in python to create a string.

str = "Hi Python !" 

# Here, if we check the type of the variable str using a python script

print(type(str)) #  then it will print string (str).  
# In python, strings are treated as the sequence of strings which means that python 
# doesn't support the character data type instead a single character written as 'p' is treated as the string of length 1.


# Strings indexing and splitting
# Like other languages, the indexing of the python strings starts from 0. 
# For example, The string "HELLO" is indexed as given in the below figure.
# As shown in python, the slice operator [] is used to access the individual characters of the string. 
# However, we can use the : (colon) operator in python to access the substring. Consider the following example.

# str[0] => H
# str[1] => E
# str[2] => L
# str[3] => L
# str[4] => O
# str[:] => HELLO
# str[0:] => HELLO
# str[:5] => HELLO
# str[:3] => HEL
# str[0:2] => HE
# str[1:4] => ELL


# Reassigning strings
# Updating the content of the strings is as easy as assigning it to a new string. The string object doesn't support item assignment i.e., A string can only be replaced with a new string since its content can not be partially replaced. Strings are immutable in python.

# Consider the following example.

# Example 1
# str = "HELLO"  
# str[0] = "h"  
# print(str)  


# Output:
# Traceback (most recent call last):
#   File "12.py", line 2, in <module>
#     str[0] = "h";
# TypeError: 'str' object does not support item assignment


# However, in example 1, the string str can be completely assigned to a new content as specified in the following example.

# Example 2
# str = "HELLO"  
# print(str)  
# str = "hello"  
# print(str)  


# Output:
# HELLO
# hello  