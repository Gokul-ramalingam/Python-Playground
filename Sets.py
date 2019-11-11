# Python Set
# The set in python can be defined as the unordered collection of various items enclosed within the curly braces. 
# The elements of the set can not be duplicate. The elements of the python set must be immutable.

# Unlike other collections in python, there is no index attached to the elements of the set, 
# i.e., we cannot directly access any element of the set by the index. 
# However, we can print them all together or we can get the list of elements by looping through the set.

# Creating a set
# The set can be created by enclosing the comma separated items with the curly braces.
#  Python also provides the set method which can be used to create the set by the passed sequence.


# Example 1: using curly braces

Days = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
print(Days)
print(type(Days))

print("looping through the set elements ... ")  
for i in Days:
    print(i)

# Example 2: using set() method
Days = set(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
print(Days)
print(type(Days))
print("looping through the set elements ... ")  
for i in Days:
    print(i)




# Python Set
# The set in python can be defined as the unordered collection of various items enclosed within the curly braces. 
# The elements of the set can not be duplicate. The elements of the python set must be immutable.

# Unlike other collections in python, there is no index attached to the elements of the set, i.e., 
# we cannot directly access any element of the set by the index.
#  However, we can print them all together or we can get the list of elements by looping through the set.

# Creating a set
# The set can be created by enclosing the comma separated items with the curly braces. 
# Python also provides the set method which can be used to create the set by the passed sequence.

# Example 1: using curly braces
Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}  
print(Days)  
print(type(Days))  
print("looping through the set elements ... ")  
for i in Days:  
    print(i)  

# Example 2: using set() method
Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])  
print(Days)  
print(type(Days))  
print("looping through the set elements ... ")  
for i in Days:  
    print(i)  



# Python Set operations
# In the previous example, we have discussed about how the set is created in python. 
# However, we can perform various mathematical operations on python sets like union, intersection, difference, etc.
Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nAdding other months to the set...")
Months.add("July") 
Months.add("August") 
print("\nPrinting the modified set...")
print(Months)  
print("\nlooping through the set elements ... ")  
for i in Months:  
    print(i)  

# To add more than one item in the set, Python provides the update() method.
Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nupdating the original set ... ")  
Months.update(["July","August","September","October"])
print("\nprinting the modified set ... ")   
print(Months)

# Removing items from the set
# Python provides discard() method which can be used to remove the items from the set.
Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nRemoving some months from the set...")
Months.discard("January")
Months.discard("May")
print("\nPrinting the modified set...")
print(Months)  
print("\nlooping through the set elements ... ")  
for i in Months:  
    print(i)  


# Python also provide the remove() method to remove the items from the set.
Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nRemoving some months from the set...")
Months.remove("January")
Months.remove("May")
print("\nPrinting the modified set...") 
print(Months)  

# We can also use the pop() method to remove the item. However, this method will always remove the last item.
Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nRemoving some months from the set...") 
Months.pop() 
Months.pop() 
print("\nPrinting the modified set...")
print(Months)  

# python provides the clear() method to remove all the items from the set.
Months = set(["January","February", "March", "April", "May", "June"])  
print("\nprinting the original set ... ")  
print(Months)  
print("\nRemoving all the items from the set...");  
Months.clear()  
print("\nPrinting the modified set...")  
print(Months)  


# Difference between discard() and remove()
# Despite the fact that discard() and remove() method both perform the same task, 
# There is one main difference between discard() and remove().

# If the key to be deleted from the set using discard() doesn't exist in the set, the python will not give the error. 
# The program maintains its control flow.

# On the other hand, if the item to be deleted from the set using remove() doesn't exist in the set, the python will give the error.

