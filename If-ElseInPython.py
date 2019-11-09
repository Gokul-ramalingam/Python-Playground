# The if-else statement
# The if-else statement provides an else block combined with the if statement which is executed in the false case of the condition.

# If the condition is true, then the if-block is executed. Otherwise, the else-block is executed.

# The syntax of the if-else statement is given below.

# if condition:
# block of statements
# else:
# another block of statements (else-block)

# Program to check whether a person is eligible to vote or not

age = int(input("Enter your age?"))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Program to check wheather a number is positve or not
num = int(input("Enter the number?"))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
