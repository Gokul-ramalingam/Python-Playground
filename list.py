# List in python is implemented to store the sequence of various type of data. 
# However, python contains six data types that are capable to store the sequences but the most common and reliable type is list.

# A list can be defined as a collection of values or items of different types. 
# The items in the list are separated with the comma (,) and enclosed with the square brackets [].

# L1 = ["John", 102, "USA"]  
# L2 = [1, 2, 3, 4, 5, 6]  
# L3 = [1, "Ryan"]  

# If we try to print the type of L1, L2, and L3 then it will come out to be a list.

# Lets consider a proper example to define a list and printing its values.
emp = ["John", 102, "USA"]   
Dep1 = ["CS",10]
Dep2 = ["IT",11]
HOD_CS = [10,"Mr. Holding"]  
HOD_IT = [11, "Mr. Bewon"]  
print("printing employee data...")
print("Name : %s, ID: %d, Country: %s"%(emp[0],emp[1],emp[2]))  
print("printing departments...")
print("Department 1:\nName: %s, ID: %d\nDepartment 2:\nName: %s, ID: %s"%(Dep1[0],Dep2[1],Dep2[0],Dep2[1]))
print("HOD Details ....")
print("CS HOD Name: %s, Id: %d"%(HOD_CS[1],HOD_CS[0]))
print("IT HOD Name: %s, Id: %d"%(HOD_IT[1],HOD_IT[0]))
print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))


# List indexing and splitting
# The indexing are processed in the same way as it happens with the strings. 
# The elements of the list can be accessed by using the slice operator [].

# The index starts from 0 and goes to length - 1. 
# The first element of the list is stored at the 0th index, the second element of the list is stored at the 1st index, and so on.

# Unlike other languages, python provides us the flexibility to use the negative indexing also. 
# The negative indices are counted from the right. The last element (right most) of the list has the index -1,
#  its adjacent left element is present at the index -2 and so on until the left most element is encountered.
List = [0,1,2,3,4,5]
# index in forward direction = [0,1,2,3,4,5]
# index in backward direction = [-6,-5,-4,-3,-2,-1]


# Updating List values
# Lists are the most versatile data structures in python since they are immutable and their values can be updated by using the slice and assignment operator.

# Python also provide us the append() method which can be used to add values to the string.

List = [1, 2, 3, 4, 5, 6]   
print(List)   
List[2] = 10
print(List)  
List[1:3] = [89, 78]   
print(List)  

# Output:

# [1, 2, 3, 4, 5, 6]
# [1, 2, 10, 4, 5, 6]
# [1, 89, 78, 4, 5, 6]

# The list elements can also be deleted by using the del keyword. 
# Python also provides us the remove() method if we do not know which element is to be deleted from the list.

# Consider the following example to delete the list elements.

List = [0,1,2,3,4]   
print(List)  
del List[0]  
print(List)   
del List[3]  
print(List) 

# Output:

# [0, 1, 2, 3, 4]
# [1, 2, 3, 4]
# [1, 2, 3]

# Python List Operations
# The concatenation (+) and repetition (*) operator work in the same way as they were working with the strings.

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]  



# Repetition	The repetition operator enables the list elements to be repeated multiple times.	
# L1*2 = [1, 2, 3, 4, 1, 2, 3, 4]
# Concatenation	It concatenates the list mentioned on either side of the operator.	
# l1+l2 = [1, 2, 3, 4, 5, 6, 7, 8]
# Membership	It returns true if a particular item exists in a particular list otherwise false.	
# print(2 in l1) prints True.
# Iteration	The for loop is used to iterate over the list elements.	
# for i in l1: 
#     print(i)
# Output
# 1
# 2
# 3
# 4
# Length	It is used to get the length of the list	
# len(l1) = 4

# Iterating a List
# A list can be iterated by using a for - in loop. A simple list containing four strings can be iterated as follows.

# List = ["John", "David", "James", "Jonathan"]  
# for i in List: #i will iterate over the elements of the List and contains each element in each iteration.   
#     print(i);  

# Output:

# John
# David
# James
# Jonathan

# Adding elements to the list
# Python provides append() function by using which we can add an element to the list. 
# However, the append() method can only add the value to the end of the list.
l =[]
n = int(input("Enter the number of elements in the list"))#Number of elements will be entered by the user  
for i in range(0,n):# for loop to take the input  
    l.append(input("Enter the item?"))# The input is taken from the user and added to the list as the item  
print("printing the list items....")  
for i in l: # traversal loop to print the list items  
    print(i, end = "  ")

# Output:

# Enter the number of elements in the list 5
# Enter the item?1
# Enter the item?2
# Enter the item?3
# Enter the item?4
# Enter the item?5
# printing the list items....
# 1  2  3  4  5 


# Removing elements from the list
# List = [0,1,2,3,4]   
# print("printing original list: ");  
# for i in List:  
#     print(i,end=" ")  
# List.remove(0)  
# print("\nprinting the list after the removal of first element...")  
# for i in List:  
#     print(i,end=" ")  


# Output:

# printing original list: 
# 0 1 2 3 4 
# printing the list after the removal of first element...
# 1 2 3 4  

# Python List Built-in functions
# Python provides the following built-in functions which can be used with the lists.

# SN	Function	Description
# 1	cmp(list1, list2)	It compares the elements of both the lists.
# 2	len(list)	It is used to calculate the length of the list.
# 3	max(list)	It returns the maximum element of the list.
# 4	min(list)	It returns the minimum element of the list.
# 5	list(seq)	It converts any sequence to the list.


# Python List built-in methods
# SN	Function	Description
# 1	list.append(obj)	The element represented by the object obj is added to the list.
# 2	list.clear()	It removes all the elements from the list.
# 3	List.copy()	It returns a shallow copy of the list.
# 4	list.count(obj)	It returns the number of occurrences of the specified object in the list.
# 5	list.extend(seq)	The sequence represented by the object seq is extended to the list.
# 6	list.index(obj)	It returns the lowest index in the list that object appears.
# 7	list.insert(index, obj)	The object is inserted into the list at the specified index.
# 8	list.pop(obj=list[-1])	It removes and returns the last object of the list.
# 9	list.remove(obj)	It removes the specified object from the list.
# 10	list.reverse()	It reverses the list.
# 11	list.sort([func])	It sorts the list by using the specified compare function if given.