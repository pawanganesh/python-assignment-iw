# Make pythonic solutions for each of the follwing data structure
# and algorithm problems.

# g) Interpolation Search

def interpolation_search(arr, n, x):
    l = 0
    h = (n - 1)

    while l <= h and x >= arr[l] and x <= arr[h]:
        if l == h:
            if arr[l] == x:
                return l
            return -1

        pos = l + int(((float(h - l) / (arr[h] - arr[l])) * (x - arr[l])))

        if arr[pos] == x:
            return pos

        if arr[pos] < x:
            l = pos + 1
        else:
            h = pos - 1

    return -1

lst = [2, 4, 6, 8, 9, 10, 12, 14, 16, 18]
n = len(lst)
x = 14
print(interpolation_search(lst, n, x))
