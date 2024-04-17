 
# def isItExists(x):
#  if x in d:
#   print("Key is Already in dict")
#  else:
#   print("key in not in the dict")

# isItExists(4)



d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
 
 
def isItExists(x):
 if x in d.values():
  print("values is Already in dict")
 else:
  print("values is not in the dict")

isItExists(40)