# Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.


str1 = "nythop"

first_char = str1[0]
last_char = str1[-1]
middle_char = str1[1:-1]

result = last_char + middle_char + first_char
print(result)
