# Python while loop
# The while loop is also known as a pre-tested loop. 
# In general, a while loop allows a part of the code to be executed as long as the given condition is true.

# It can be viewed as a repeating if statement. 
# The while loop is mostly used in the case where the number of iterations is not known in advance.

# The syntax is given below.

# while expression:  
#     statements  

i = 1
while i <= 10:
    print(i)
    i = i+1

# Infinite while loop
# If the condition given in the while loop never becomes false then the while loop will never terminate and result into the infinite while loop.

# Any non-zero value in the while loop indicates an always-true condition whereas 0 indicates the always-false condition. 
# This type of approach is useful if we want our program to run continuously in the loop without any disturbance.

while (1):  
    print("Hi! we are inside the infinite while loop")