# Write a Python program to add an item in a tuple.

tupl = ('Pawanlal', 1999, 'Jhapa')

def add_item(item):
    new_tupl = tupl + (item,)
    print(new_tupl)

add_item('programming')


