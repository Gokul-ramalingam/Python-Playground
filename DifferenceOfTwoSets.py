# Difference of two sets
# The difference of two sets can be calculated by using the subtraction (-) operator. 
# The resulting set will be obtained by removing all the elements from set 1 that are present in set 2.

# Example 1 : using subtraction ( - ) operator
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}  
Days2 = {"Monday", "Tuesday", "Sunday"}  
print(Days1-Days2) #{"Wednesday", "Thursday" will be printed}  

# Example 2 : using difference() method
Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}  
Days2 = {"Monday", "Tuesday", "Sunday"}  
print(Days1.difference(Days2)) # prints the difference of the two sets Days1 and Days2 