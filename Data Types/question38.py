# Write a Python program to remove a key from a dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}

def remove_key(key):
    del dic[key]
    print(dic)

remove_key(3)
