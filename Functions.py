# Python Functions
# Functions are the most important aspect of an application. 
# A function can be defined as the organized block of reusable code which can be called whenever required.

# Python allows us to divide a large program into the basic building blocks known as function. 
# The function contains the set of programming statements enclosed by {}.
#  A function can be called multiple times to provide reusability and modularity to the python program.

# In other words, we can say that the collection of functions creates a program. 
# The function is also known as procedure or subroutine in other programming languages.

# Python provide us various inbuilt functions like range() or print(). 
# Although, the user can create its functions which can be called user-defined functions.

# Advantage of functions in python
# There are the following advantages of C functions.

# By using functions, we can avoid rewriting same logic/code again and again in a program.
# We can call python functions any number of times in a program and from any place in a program.
# We can track a large python program easily when it is divided into multiple functions.
# Reusability is the main achievement of python functions.
# However, Function calling is always overhead in a python program.

# Creating a function
# In python, we can use def keyword to define the function. The syntax to define a function in python is given below.

# def my_function():  
#     function-suite   
#     return <expression>   

# The function block is started with the colon (:) and all the same level block statements remain at the same indentation.

# A function can accept any number of parameters that must be the same in the definition and function calling.

# Function calling
# In python, a function must be defined before the function calling otherwise the python interpreter gives an error. 
# Once the function is defined, we can call it from another function or the python prompt. 
# To call the function, use the function name followed by the parentheses.

def helloworld():
    print("Hello World!")

helloworld();


# Parameters in function
# The information into the functions can be passed as the parameters. 
# The parameters are specified in the parentheses. 
# We can give any number of parameters, but we have to separate them with a comma.

# Example 1

def func(name):
    print("Hi",name)

func("John")


# Example 2

def add(a,b):
    return a+b;

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("sum = ",add(a,b))


# Call by reference in Python

# Call by reference in Python
# In python, all the functions are called by reference,
#  i.e., all the changes made to the reference inside the function revert back to the original value referred by the reference.

# However, there is an exception in the case of mutable objects since the changes made to the mutable objects like string
#  do not revert to the original string rather, a new string object is made, and therefore the two different objects are printed.


# Example 1 Passing Immutable Object (String)
#defining the function  
def change_string (str):  
    str = str + " Hows you";  
    print("printing the string inside function :",str);  
  
string1 = "Hi I am there"  
  
#calling the function  
change_string(string1)  
  
print("printing the string outside function :",string1)

# Output:

# printing the string inside function : Hi I am there Hows you
# printing the string outside function : Hi I am there


# Example 2 Passing Mutable Object (List)

#defining the function  
def change_list(list1):  
    list1.append(20)
    list1.append(30)
    print("list inside function = ",list1)  
  
#defining the list  
list1 = [10,30,40,50]  
  
#calling the function   
change_list(list1)
print("list outside function = ",list1)

# Output:

# list inside function =  [10, 30, 40, 50, 20, 30]
# list outside function =  [10, 30, 40, 50, 20, 30]

# Required Arguments


# Till now, we have learned about function calling in python. 
# However, we can provide the arguments at the time of function calling. 
# As far as the required arguments are concerned, these are the arguments which are required to be passed at the time of function calling with the exact match of their positions in the function call and function definition. 
# If either of the arguments is not provided in the function call, or the position of the arguments is changed, then the python interpreter will show the error.

# Example 1
#the argument name is the required argument to the function func   
def func1(name):  
    message = "Hi "+name
    return message
name = input("Enter the name?")  
print(func1(name)) 

# Example 2
#the function simple_interest accepts three arguments and returns the simple interest accordingly  
def simple_interest(p,t,r):  
    return (p*t*r)/100  
p = float(input("Enter the principle amount? "))  
r = float(input("Enter the rate of interest? "))  
t = float(input("Enter the time in years? "))  
print("Simple Interest: ",simple_interest(p,r,t)) 

# Keyword arguments
# Python allows us to call the function with the keyword arguments. 
# This kind of function call will enable us to pass the arguments in the random order.

# The name of the arguments is treated as the keywords and matched in the function calling and definition.
#  If the same match is found, the values of the arguments are copied in the function definition.

# Consider the following example.
# Example 1
#function func is called with the name and message as the keyword arguments  
def func2(name,message):  
    print("printing the message with",name,"and ",message)  
func2(name = "John",message="hello") #name and message is copied with the values John and hello respectively

# Example 2 providing the values in different order at the calling
#The function simple_interest(p, t, r) is called with the keyword arguments the order of arguments doesn't matter in this case  
def simple_interest1(p,t,r):  
    return (p*t*r)/100  
print("Simple Interest: ",simple_interest1(t=10,r=10,p=1900))   


# The python allows us to provide the mix of the required arguments and keyword arguments at the time of function call. 
# However, the required argument must not be given after the keyword argument, i.e., once the keyword argument is encountered in the function call, the following arguments must also be the keyword arguments.
# Example 4
def func3(name1,message,name2):  
    print("printing the message with",name1,",",message,",and",name2)  
func3("John",message="hello",name2="David") #the first argument is not the keyword argument  

# Output:

# printing the message with John , hello ,and David

# Default Arguments
# Python allows us to initialize the arguments at the function definition.
#  If the value of any of the argument is not provided at the time of function call, 
#  then that argument can be initialized with the value given in the definition even 
#  if the argument is not specified at the function call.
# Example 1 
def printme(name,age=22):  
    print("My name is",name,"and age is",age)  
printme(name = "john") #the variable age is not passed into the function however the default value of age is cons

# Output:

# My name is john and age is 22

def printme1(name,age=22):  
    print("My name is",name,"and age is",age)  
printme1(name = "john") #the variable age is not passed into the function however the default value of age is considered in the function  
printme1(age = 10,name="David") #the value of age is overwritten here, 10 will be printed as age 

# Variable length Arguments
# In the large projects, sometimes we may not know the number of arguments to be passed in advance.
#  In such cases, Python provides us the flexibility to provide the comma separated values which are internally treated as tuples at the function call.

# However, at the function definition, we have to define the variable with * (star) as *<variable - name >.
# Example
def printme2(*names):  
    print("type of passed argument is ",type(names))  
    print("printing the passed arguments...")  
    for name in names:  
        print(name)  
printme2("john","David","smith","nick")