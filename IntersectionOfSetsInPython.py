# Intersection of two sets
# The & (intersection) operator is used to calculate the intersection of the two sets in python. 
# The intersection of the two sets are given as the set of the elements that common in both sets.


# Example 1: using & operator
set1 = {"Ayush","John", "David", "Martin"}  
set2 = {"Steve","Milan","David", "Martin"}  
print(set1&set2) #prints the intersection of the two sets


# Example 2: using intersection() method
set1 = {"Ayush","John", "David", "Martin"}  
set2 = {"Steave","Milan","David", "Martin"}  
print(set1.intersection(set2)) #prints the intersection of the two sets  

# The intersection_update() method removes the items from the original set that are not present in both the sets (all the sets if more than one are specified).

# The Intersection_update() method is different from intersection() method 
# since it modifies the original set by removing the unwanted items, on the other hand, intersection() method returns a new set.
a = {"ayush", "bob", "castle"}  
b = {"castle", "dude", "emyway"}  
c = {"fuson", "gaurav", "castle"}  
  
a.intersection_update(b, c)  
  
print(a)  