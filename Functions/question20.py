# Write a Python program to find intersection of two given arrays using
# Lambda.

arr1 = [1, 2, 3, 4, 5, 6, 7, 9]
arr2 = [2, 4, 6, 8, 10]

result = list(filter(lambda x: x in arr1, arr2))

print(result)