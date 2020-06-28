# Write a Python program to multiplies all the items in a list.

from functools import reduce

lst = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x*y, lst)
print(result)