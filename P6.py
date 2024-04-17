#Write a Python program to calculate the sum of the positive and negative numbers
#of a given list of numbers using the lambda function.
 
# Create a list named 'nums' containing integers, including both positive and negative numbers
 
#nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
num = [2,4,-6,-9,11,-12,-13,7,9,-23]
sumn = sum(filter(lambda x:x<0,num))
sump = sum(filter(lambda x:x>0,num))
 
print("sum of positive numbers is ",sump)
print("sum of negative numbers is ",sumn)