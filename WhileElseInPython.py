# Using else with Python while loop
# Python enables us to use the while loop with the while loop also. 
# The else block is executed when the condition given in the while statement becomes false.
#  Like for loop, if the while loop is broken using break statement, 
# then the else block will not be executed and the statement present after else block will be executed.

i=1 
while i<=5:  
    print(i)  
    i=i+1
else:print("The while loop exhausted")

i=1  
while i<=5:  
    print(i)  
    i=i+1
    if(i==3):  
        break
else:print("The while loop exhausted")