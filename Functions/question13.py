# Write a Python program to sort a list of tuples using Lambda.

lst = [(4, 1), (1, 2), (2, 1), (5, 4), (3, 4)]

func_sort = lambda x: x[0]

lst.sort(key=func_sort)
print(lst)
