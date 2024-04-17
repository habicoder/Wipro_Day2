#Write a Python program to calculate the sum of the positive and negative numbers
#of a given list of numbers using the lambda function.
 
# Create a list named 'nums' containing integers, including both positive and negative numbers
 
#nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
s=[2,4,-6,-9,11,-12,14,-5,17]

c= sum(filter(lambda x: x > 0, s))
y= sum(filter(lambda x: x < 0, s))
print("Sum of positive numbers:", c)
print("Sum of negative numbers:", y)