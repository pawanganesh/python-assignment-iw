# Write a Python program to filter a list of integers using Lambda.

even  = lambda x: x % 2 == 0
odd  = lambda x: x % 2 != 0


lst = [13, 54, 56, 34, 12, 23, 24, 12, 33, 11]

lst_even = list(filter(even, lst))
lst_odd = list(filter(odd, lst))

print(lst_even)
print(lst_odd)