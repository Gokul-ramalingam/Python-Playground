# Python continue Statement
# The continue statement in python is used to bring the program control to the beginning of the loop. 
# The continue statement skips the remaining lines of code inside the loop and start with the next iteration.
#  It is mainly used for a particular condition inside the loop so that we can skip some specific code for a particular condition.

# The syntax of Python continue statement is given below.

#loop statements  
# continue;  
#the code to be skipped   
i=1; #initializing a local variable  
#starting a loop from 1 to 10  
for i in range(1,11):  
    if i==5:  
        continue;  
    print("%d"%i);  

 