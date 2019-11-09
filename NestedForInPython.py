# Python allows us to nest any number of for loops inside a for loop. 
# The inner loop is executed n number of times for every iteration of the outer loop. 
# The syntax of the nested for loop in python is given below.

# Python allows us to nest any number of for loops inside a for loop. 
# The inner loop is executed n number of times for every iteration of the outer loop. 
# The syntax of the nested for loop in python is given below.

# for iterating_var1 in sequence:  
#     for iterating_var2 in sequence:  
        #block of statements   

#Other statements  
n = int(input("Enter number of rows you want to print?"))
i,j = 0,0;
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end=" ")
     

