# Write a Python program to get the largest number from a list.


lst = [34, 67, 34, 90, 87, 150]

result = 0
for num in lst:
    if num > result:
        result = num
print(result)
