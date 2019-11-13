# Scope of variables
# The scopes of the variables depend upon the location where the variable is being declared. 
# The variable declared in one part of the program may not be accessible to the other parts.

# In python, the variables are defined with the two types of scopes.

# Global variables
# Local variables
# The variable defined outside any function is known to have a global scope 
# whereas the variable defined inside a function is known to have a local scope.

# Example 1
def print_message():  
    message = "hello !! I am going to print a message." # the variable message is local to the function itself  
    print(message)  
print_message()  
# print(message) # this will cause an error since a local variable cannot be accessible here.


def calculate(*args):  
    sum=0  
    for arg in args:  
        sum = sum +arg  
    print("The sum is",sum)  
sum=0  
calculate(10,20,30) #60 will be printed as the sum  
print("Value of sum outside the function:",sum) # 0 will be printed  