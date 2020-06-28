# Write a Python program to find the index of an item of a tuple.


tupl = ('Python', 'is', 'fun', 'to', 'learn', 'and', 'it\'s', 'awesome', 'language')

def index_finder(item):
    index = tupl.index(item)
    print(item,index)

index_finder('Python')
index_finder('fun')
index_finder('awesome')