# Make pythonic solutions for each of the following data structure
# and algorithm problems.
# d) Merge Sort

def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        l = lst[:mid]
        r = lst[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lst[k] = l[i]
                i += 1
            else:
                lst[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            lst[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            lst[k] = r[j]
            j += 1
            k += 1

lst = [46, 43, 27, 57, 41, 45, 21]
merge_sort(lst)
print(lst)
