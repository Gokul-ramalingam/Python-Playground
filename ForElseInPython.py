# Using else statement with for loop
# Unlike other languages like C, C++, or Java, python allows us to use the else statement with the for loop which can be executed only when all the iterations are exhausted. 
# Here, we must notice that if the loop contains any of the break statement then the else statement will not be executed.

for i in range(0,5):
    print(i)
else:
    print("For loop completely exhausted, since there is no break.");
# In the above example, for loop is executed completely since there is no break statement in the loop. 
# The control comes out of the loop and hence the else block is executed.

for i in range(0,5):  
    print(i)  
    break;  
else:print("for loop is exhausted");
# Here the for loop got broken because of break so the else statement won't work