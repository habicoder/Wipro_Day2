d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_value_present(x):
    if x in d.values():
       print(x, ' value is present in the dictionary')
    else:
       print(x, ' value is not present in the dictionary')
 
is_value_present(10)