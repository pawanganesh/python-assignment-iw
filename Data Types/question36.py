# Write a Python program to sum all the items in a dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

sum = 0
for value in dic.values():
    sum += value
print(sum)