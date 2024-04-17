'''Write a Python program to get the maximum and minimum values of a dictionary.
 
Sample Solution:-
 
Python Code:
 
# Create a dictionary 'my_dict' with key-value pairs.
 
my_dict = {'x': 500, 'y': 5874, 'z': 560}'''

my_dict = {'x': 500, 'y': 5874, 'z': 560}
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Max val:", max_value)
print("Min val:", min_value)