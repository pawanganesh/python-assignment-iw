# Write a Python script to check whether a given key already exists in a
# dictionary.


dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def key_checker(key):
    for i in dic.keys():
        if i == key:
            return 'Key already exists'
    return 'Key does not exist'

print(key_checker(5))