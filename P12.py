'''
Write a Python program that creates a list of dictionaries containing student information (name, age, grade)
 
and uses the filter function to extract students with a grade greater than or equal to 95.
 
Sample Solution:
 
students = [
          	  {"name": "Denis Helio", "age": 17, "grade": 97},
   	          {"name": "Hania Mehtap", "age": 16, "grade": 92},
    		  {"name": "Kelan Stasys", "age": 17, "grade": 90},
   		  {"name": "Velvet Mirko", "age": 16, "grade": 94},
   	          {"name": "Delores Aeneas", "age": 17, "grade": 100}
 '''
 
students = [
           {"name": "Denis Helio", "age": 17, "grade": 97},
           {"name": "Hania Mehtap", "age": 16, "grade": 92},
           {"name": "Kelan Stasys", "age": 17, "grade": 90},
           {"name": "Velvet Mirko", "age": 16, "grade": 94},
           {"name": "Delores Aeneas", "age": 17, "grade": 100},
           ]
 
print(list(filter(lambda x: x ["grade"] >= 95, students)))