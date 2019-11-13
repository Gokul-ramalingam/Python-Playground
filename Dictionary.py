# Python Dictionary
# Dictionary is used to implement the key-value pair in python. 
# The dictionary is the data type in python which can simulate the real-life data arrangement where some specific value exists for some particular key.

# In other words, we can say that a dictionary is the collection of key-value pairs where the value can be any python object whereas the keys are the immutable python object, i.e., Numbers, string or tuple.

# Dictionary simulates Java hash-map in python.

# Creating the dictionary
# The dictionary can be created by using multiple key-value pairs enclosed with the small brackets () and separated by the colon (:). 
# The collections of the key-value pairs are enclosed within the curly braces {}.

# The syntax to define the dictionary is given below.

Dict = {"Name": "Ayush","Age": 22}  

# In the above dictionary Dict, The keys Name, and Age are the string that is an immutable object.

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print(Employee)   


# Accessing the dictionary values
# We have discussed how the data can be accessed in the list and tuple by using the indexing.

# However, the values can be accessed in the dictionary by using the keys as keys are unique in the dictionary.

# The dictionary values can be accessed in the following way.

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print("Name : %s" %Employee["Name"])  
print("Age : %d" %Employee["Age"])  
print("Salary : %d" %Employee["salary"])  
print("Company : %s" %Employee["Company"])

# Python provides us with an alternative to use the get() method to access the dictionary values. 
# It would give the same result as given by the indexing.

# Updating dictionary values
# The dictionary is a mutable data type, and its values can be updated by using the specific keys.
Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print(Employee)  
print("Enter the details of the new employee....")
Employee["Name"] = input("Name: ")
Employee["Age"] = int(input("Age: "))
Employee["salary"] = int(input("Salary: "))  
Employee["Company"] = input("Company:") 
print("printing the new data") 
print(Employee)


# Deleting elements using del keyword

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
print(type(Employee))  
print("printing Employee data .... ")  
print(Employee)  
print("Deleting some of the employee data")   
del Employee["Name"]  
del Employee["Company"]  
print("printing the modified information ")  
print(Employee)  
print("Deleting the dictionary: Employee")
del Employee  
print("Lets try to print it again ")
print(Employee)

# Iterating Dictionary
# A dictionary can be iterated using the for loop as given below.
# for loop to print all the keys of a dictionary

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
for x in Employee:  
    print(x)

#for loop to print all the values of the dictionary

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
for x in Employee:  
    print(Employee[x])

#for loop to print the values of the dictionary by using values() method.

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
for x in Employee.values():  
    print(x)

#for loop to print the items of the dictionary by using items() method.

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}  
for x in Employee.items():  
    print(x)

# In the dictionary, we can not store multiple values for the same keys. 
# If we pass more than one values for a single key, then the value which is last assigned is considered as the value of the key.

Employee = {"Name": "John", "Age": 29, "Salary":25000,"Company":"GOOGLE","Name":"Johnn"}  
for x,y in Employee.items():  
    print(x,y)  


# In python, the key cannot be any mutable object. We can use numbers, strings, or 
# tuple as the key but we can not use any mutable object like the list as the key in the dictionary.

# Consider the following example.

Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,301]:"Department ID"}  
for x,y in Employee.items():  
    print(x,y)  


# Output:

# Traceback (most recent call last):
#   File "list.py", line 1, in 
#     Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE",[100,201,301]:"Department ID"}
# TypeError: unhashable type: 'list'
