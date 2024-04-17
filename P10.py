'''
Write a Python program to drop empty items from a given dictionary.
 
# Create a dictionary 'dict1' with keys and associated values, including a 'None' value.
 
dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
'''
'''dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
del dict1["c3"]
print(dict1)'''

dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
dict1 = {key: value for key, value in dict1.items() if value is not None}
print("Dictionary after removing empty items:", dict1)