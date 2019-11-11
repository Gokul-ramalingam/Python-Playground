# FrozenSets
# The frozen sets are the immutable form of the normal sets, 
# i.e., the items of the frozen set can not be changed and therefore it can be used as a key in dictionary.

# The elements of the frozen set can not be changed after the creation. 
# We cannot change or append the content of the frozen sets by using the methods like add() or remove().

# The frozenset() method is used to create the frozenset object. 
# The iterable sequence is passed into this method which is converted into the frozen set as a return type of the method.

Frozenset = frozenset([1,2,3,4,5])   
print(type(Frozenset))  
print("\nprinting the content of frozen set...")  
for i in Frozenset:  
    print(i)
# Frozenset.add(6) #gives an error since we cannot change the content of Frozenset after creation   


# Frozenset for the dictionary
# If we pass the dictionary as the sequence inside the frozenset() method, 
# it will take only the keys from the dictionary and returns a frozenset that contains the key of the dictionary as its elements.
Dictionary = {"Name":"John", "Country":"USA", "ID":101}   
print(type(Dictionary))  
Frozenset = frozenset(Dictionary) #Frozenset will contain the keys of the dictionary  
print(type(Frozenset))  
for i in Frozenset:   
    print(i)  