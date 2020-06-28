# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

# Sample List : ​ [1,2,3,3,3,3,4,5]
# Unique List : ​ [1, 2, 3, 4, 5]

result = []
def unique(lst):
    for i in lst:
        if i not in result:
            result.append(i)
    return result


lst = [1,2,3,3,3,3,4,5]
print(unique(lst))