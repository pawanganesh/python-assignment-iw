# Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.

def binary_search(seq, item):
    try:
        res = seq.index(item)
        return res
    except ValueError:
        return -1

seq = [2, 5, 4, 8, 1, 10, 14]
seq.sort()
item1 = 10
item2 = 15

print(binary_search(seq, item1))
print(binary_search(seq, item2))