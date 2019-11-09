# Python Operators
# The operator can be defined as a symbol which is responsible for a particular operation between two operands. 
# Operators are the pillars of a program on which the logic is built in a particular programming language. 
# Python provides a variety of operators described as follows.

# Arithmetic operators
# Comparison operators
# Assignment Operators
# Logical Operators
# Bitwise Operators
# Membership Operators
# Identity Operators

# Arithmetic operators
# Arithmetic operators are used to perform arithmetic operations between two operands. 
# It includes +(addition), - (subtraction), *(multiplication), /(divide), %(reminder), //(floor division), and exponent (**).

a = 20
b = 10
print(a+b)
print(a-b)
print(a*b)
print(a/b)   #ouptput will be in decimal number
print(a%b)
print(b**2) #eg: 10 power 2
print(a//b) #give floor value use it instead of division


# Comparison operator
# Comparison operators are used to comparing the value of the two operands and returns boolean true or false accordingly. 
# The comparison operators are described in the following table.

print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print(a < b)
print( a > b)


# Python assignment operators
# The assignment operators are used to assign the value of the right expression to the left operand.
#  The assignment operators are described in the following table.
# =	It assigns the the value of the right expression to the left operand.
# +=	It increases the value of the left operand by the value of the right operand and assign the modified value back to left operand. For example, if a = 10, b = 20 => a+ = b will be equal to a = a+ b and therefore, a = 30.
# -=	It decreases the value of the left operand by the value of the right operand and assign the modified value back to left operand. For example, if a = 20, b = 10 => a- = b will be equal to a = a- b and therefore, a = 10.
# *=	It multiplies the value of the left operand by the value of the right operand and assign the modified value back to left operand. For example, if a = 10, b = 20 => a* = b will be equal to a = a* b and therefore, a = 200.
# %=	It divides the value of the left operand by the value of the right operand and assign the reminder back to left operand. For example, if a = 20, b = 10 => a % = b will be equal to a = a % b and therefore, a = 0.
# **=	a**=b will be equal to a=a**b, for example, if a = 4, b =2, a**=b will assign 4**2 = 16 to a.
# //=	A//=b will be equal to a = a// b, for example, if a = 4, b = 3, a//=b will assign 4//3 = 1 to a.

# Bitwise operator
# The bitwise operators perform bit by bit operation on the values of the two operands.
# & (binary and)	If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied.
# | (binary or)	The resulting bit will be 0 if both the bits are zero otherwise the resulting bit will be 1.
# ^ (binary xor)	The resulting bit will be 1 if both the bits are different otherwise the resulting bit will be 0.
# ~ (negation)	It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa.
# << (left shift)	The left operand value is moved left by the number of bits present in the right operand.
# >> (right shift)	The left operand is moved right by the number of bits present in the right operand.

# Logical Operators
# The logical operators are used primarily in the expression evaluation to make a decision. Python supports the following logical operators.
# and	If both the expression are true, then the condition will be true. If a and b are the two expressions, a → true, b → true => a and b → true.
# or	If one of the expressions is true, then the condition will be true. If a and b are the two expressions, a → true, b → false => a or b → true.
# not	If an expression a is true then not (a) will be false and vice versa.


# Membership Operators
# Python membership operators are used to check the membership of value inside a data structure. 
# If the value is present in the data structure, then the resulting value is true otherwise it returns false.

# in	- It is evaluated to be true if the first operand is found in the second operand (list, tuple, or dictionary).
# not in -	It is evaluated to be true if the first operand is not found in the second operand (list, tuple, or dictionary).


# Identity Operators
# is	- It is evaluated to be true if the reference present at both sides point to the same object.
# is not	- It is evaluated to be true if the reference present at both side do not point to the same object.


