# Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white


#str1 = input("Enter comma separated sequence of words: ")
str1 = 'red, while, black, red, green, black'

lst = str1.split(', ')
unique = []

for i in lst:
    if i not in unique:
        unique.append(i)

unique.sort()
print(', '.join(unique))
    


