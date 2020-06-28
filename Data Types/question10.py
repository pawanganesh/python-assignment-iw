# Write a Python program to remove the characters which have odd index
# values of a given string.

str1 = "pythonisawesome"
new_str = ""
for i in range(len(str1)):
    if i % 2 != 1:
        new_str += str1[i]
print(new_str)