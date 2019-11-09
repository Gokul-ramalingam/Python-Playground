# Python for loop
# The for loop in Python is used to iterate the statements or a part of the program several times. It is frequently used to traverse the data structures like list, tuple, or dictionary.

# The syntax of for loop in python is given below.

# for iterating_var in sequence:  
#     statement(s)  

for i in range(0,10):
    print(i,end=' ')

# Python for loop example : printing the table of the given number
num = int(input("Enter a number:"))
for i in range(1,11):
    print("%d x %d = %d"%(num,i,num*i))

# Nested for loop in python
# Python allows us to nest any number of for loops inside a for loop. The inner loop is executed n number of times for every iteration of the outer loop. 
# The syntax of the nested for loop in python is given below.