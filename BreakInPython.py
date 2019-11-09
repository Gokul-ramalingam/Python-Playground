# Python break statement
# The break is a keyword in python which is used to bring the program control out of the loop. The break statement breaks the loops one by one, i.e., in the case of nested loops, it breaks the inner loop first and then proceeds to outer loops. In other words, we can say that break is used to abort the current execution of the program and the control goes to the next line after the loop.

# The break is commonly used in the cases where we need to break the loop for a given condition.

# The syntax of the break is given below.

# The syntax of the break is given below.

#loop statements  
# break;   

list = [1,2,3,4]
count = 0;
for i in list:
    if i==4:
        print("Item matched")
        break
    count = count + 1
        
print("Found At index",count)
