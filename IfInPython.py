# The if statement
# The if statement is used to test a particular condition and if the condition is true, it executes a block of code known as if-block. 
# The condition of if statement can be any valid logical expression which can be either evaluated to true or false.

# The syntax of the if-statement is given below.

# if expression:  
#     statement  

num = int(input("Enter the input"))
if num%2 == 0:
    print("Given number is an even number")

# Example 2 : Program to print the largest of the three numbers

num1 = int(input("Enter the input1"))
num2 = int(input("Enter the input2"))
num3 = int(input("Enter the input3"))

if num1 > num2 and num1 > num3:
    print("num1 is the greatest number")

if num2 > num1 and num2 > num3:
   print("num2 is the greatest number")

if num3 > num1 and num3 > num2:
    print("num3 is the greatest number")







