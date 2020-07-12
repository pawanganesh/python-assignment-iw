# Make pythonic solutions for each of the following data structure
# and algorithm problems.
# e) Linear Search


def linear_search(lst, x):

    for i in range(len(lst)):
        if lst[i] == x:
            return i
    else:
        return -1

lst = [1,4,6,3,9,8]
x = 3
print(linear_search(lst, x))



