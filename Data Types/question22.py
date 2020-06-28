# ​ Write a Python program to remove duplicates from a list.

lst = [45, 67, 45, 'python', 'django', 'python']

result = []

for i in range(len(lst)):
    if lst[i] not in result:
        result.append(lst[i])

print(result)
