# Make pythonic solutions for each of the following data structure
# and algorithm problems.
# c) Quick Sort

def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1

    for j in range(low, high):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[high] = lst[high], lst[i+1]

    return i + 1

def quick_sort(lst, low, high):

    if low < high:
        pi = partition(lst, low, high)

        quick_sort(lst, low, pi-1)

        quick_sort(lst, pi+1, high)

lst = [10, 16, 8, 12, 15, 6, 3, 9, 5]
size = len(lst)
quick_sort(lst, 0, size-1)
print(lst)




