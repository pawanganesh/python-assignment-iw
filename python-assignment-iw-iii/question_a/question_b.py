# Make pythonic solutions for each of the following data structure
# and algorithm problems.
# b) Insertion Sort

def insertion_sort(lst):

    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1

        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j = j - 1

        lst[j+1] = temp

    return lst

lst = [5, 4, 10, 1, 6, 2]
print(insertion_sort(lst))
