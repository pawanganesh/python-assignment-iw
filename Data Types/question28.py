# Write a Python script to add a key to a dictionary.

# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

dict1 = {
    0: 10, 
    1: 20
    }

def add_key(key, value):
    dict1[key] = value
    print(dict1)

add_key(2, 40)
add_key('a', 50)
add_key('b', 'sixty')