# Write a Python program to insert a given string at the beginning of all items in
# a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']


lst = [1, 2, 3, 4]
str1 = 'emp'

for i in range(len(lst)):
    lst[i] = str1 + str(lst[i])

print(lst) 


