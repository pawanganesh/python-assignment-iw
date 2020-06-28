# Write a Python program to multiply all the items in a dictionary.


dic = {1: 1, 2: 4, 3: 6, 4: 8, 5: 10}

mul = 1
for value in dic.values():
    mul *= value

print(mul)
