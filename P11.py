names = ["Elita", "Vitold", "Audovacar", "Kerensa", "Ramana", "Iolanda", "Landyn"]
 
 
def starts_with_vowel(name):
    return name[0].lower() in ['a', 'e', 'i', 'o', 'u']
 
vowel_names = filter(starts_with_vowel, names)
 
print(list(vowel_names))