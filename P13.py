'''

Write a Python program that creates a list of words and use the filter function to extract words that contain more than five letters.
 
words = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]
'''

words = ["Red", "Green", "Orange", "White", "Black", "Pink", "Yellow"]
filtered_words = list(filter(lambda x: len(x) > 5, words))
 
print("more than five letter words are:", filtered_words)