# Write a Python program to sort a list of dictionaries using Lambda.

lst = [
    {'name': 'Pawan', 'age': 20},
    {'name': 'Bipin', 'age': 18},
    {'name': 'Pradip', 'age': 25},
    {'name': 'Naresh', 'age': 76},
    {'name': 'Dinesh', 'age': 45}
    ]

func_sort = lambda x: x['age']

lst.sort(key=func_sort)
print(lst)