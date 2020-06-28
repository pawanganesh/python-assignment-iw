# Write a Python program to clone or copy a list.

# import copy

lst = [50, 60, 70, 80 ,90, 100]

# Method - one
new_lst = []
for item in lst:
    new_lst.append(item)
print(new_lst)

# Method - two
# new_lst = copy.copy(lst) # Shallow Copy
# print(new_lst)

# Method - three
# new_lst = copy.deepcopy(lst) # Deepcopy
# print(new_lst)


