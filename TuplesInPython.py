# Python Tuple
# Python Tuple is used to store the sequence of immutable python objects. Tuple is similar to lists since the value of the items stored in the list can be changed whereas the tuple is immutable and the value of the items stored in the tuple can not be changed.

# A tuple can be written as the collection of comma-separated values enclosed with the small brackets. A tuple can be defined as follows.

# T1 = (101, "Ayush", 22)  
# T2 = ("Apple", "Banana", "Orange")   


tuple1 = (10, 20, 30, 40, 50, 60)  
print(tuple1)  



# Python Tuple
# Python Tuple is used to store the sequence of immutable python objects. Tuple is similar to lists since the value of the items stored in the list can be changed whereas the tuple is immutable and the value of the items stored in the tuple can not be changed.

# A tuple can be written as the collection of comma-separated values enclosed with the small brackets. A tuple can be defined as follows.

# T1 = (101, "Ayush", 22)  
# T2 = ("Apple", "Banana", "Orange")   


# Example
tuple1 = (10, 20, 30, 40, 50, 60)  
print(tuple1)  
count = 0  
for i in tuple1:  
    print("tuple1[%d] = %d"%(count, i))  
# Output:

# (10, 20, 30, 40, 50, 60)
# tuple1[0] = 10
# tuple1[0] = 20
# tuple1[0] = 30
# tuple1[0] = 40
# tuple1[0] = 50
# tuple1[0] = 60
# Example 2
# tuple1 = tuple(input("Enter the tuple elements ..."))  
# print(tuple1)  
# count = 0  
# for i in tuple1:  
#     print("tuple1[%d] = %s"%(count, i));  
# Output:

# Enter the tuple elements ...12345
# ('1', '2', '3', '4', '5')
# tuple1[0] = 1
# tuple1[0] = 2
# tuple1[0] = 3
# tuple1[0] = 4
# tuple1[0] = 5
# However, if we try to reassign the items of a tuple, we would get an error as the tuple object doesn't support the item assignment.

# An empty tuple can be written as follows.

# T3 = ()  
# The tuple having a single value must include a comma as given below.

# T4 = (90,)   
# A tuple is indexed in the same way as the lists. The items in the tuple can be accessed by using their specific index value.

# Nesting List and tuple
# We can store list inside tuple or tuple inside the list up to any number of level.

# Lets see an example of how can we store the tuple inside the list.

Employees = [(101, "Ayush", 22), (102, "john", 29), (103, "james", 45), (104, "Ben", 34)]  
print("----Printing list----")  
for i in Employees:  
    print(i)  
Employees[0] = (110, "David",22)  
print()
print("----Printing list after modification----")
for i in Employees:   
    print(i)