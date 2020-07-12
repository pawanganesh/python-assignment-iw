# Make pythonic solutions for each of the following data structure
# and algorithm problems.

# f) Binary Search

def binary_search(lst, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            return binary_search(lst, low, mid-1, x)
        else:
            return binary_search(lst, mid + 1, high, x)
    else:
        return -1


lst = [ 6, 12, 23, 145, 89 ]
x = 23
print(binary_search(lst, 0, len(lst)-1, x))
