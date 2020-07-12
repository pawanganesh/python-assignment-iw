# Make pythonic solutions for each of the following data structure
# and algorithm problems.
# a) Bubble Sort

def bubble_sort(lst):
    n = len(lst)

    for i in range(n-1):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

lst = [5, 1, 4, 3, 8]
print(bubble_sort(lst))


