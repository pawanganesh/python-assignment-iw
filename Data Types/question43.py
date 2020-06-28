# Write a Python program to remove an item from a tuple.

tupl = ('Python', 'is', 'fun', 'to', 'learn')

def remove_item(item):
    lst = list(tupl)
    lst.remove(item)
    print(tuple(lst))

remove_item('is')