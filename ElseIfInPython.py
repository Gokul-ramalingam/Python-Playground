# The elif statement
# The elif statement enables us to check multiple conditions and execute the specific block of statements depending upon the true condition among them.
# We can have any number of elif statements in our program depending upon our need. However, using elif is optional.

# The elif statement works like an if-else-if ladder statement in C. It must be succeeded by an if statement.

# The syntax of the elif statement is given below.

# if expression 1:
# block of statements

# elif expression 2:
# block of statements

# elif expression 3:
# block of statements

# else:
# block of statements

# Example 1
number = int(input("Enter a number?"))

if number == 10:
    print('number is equal to 10')
elif number == 50:
    print('number is equal to 50')
elif number == 100:
    print('number is equal to 100')
else:
    print("Given number is not equal to 10,50 or 100")

    # Example 2

    marks = int(input("Enter the marks?"))
    if marks <= 100 and marks > 85:
        print("You have scored A grade")
    elif marks > 60 and marks <= 85:
        print("You have scored B grade")
    elif marks > 40 and marks <= 60:
        print("You have scored C grade")
    else:
        print("You have scored F grade")
