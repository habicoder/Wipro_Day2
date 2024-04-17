#Write a Python script to check whether a given key already exists in a dictionary using a function
 
# Create a dictionary 'd' with key-value pairs.
 
 
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
       print(x, ' Key is present in the dictionary')
    else:
       print(x, ' Key is not present in the dictionary')
 
is_key_present(5)
is_key_present(9) 
    