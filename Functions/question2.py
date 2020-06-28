# Write a Python function to sum all the numbers in a list.

# Sample List : ​ (8, 2, 3, 0, 7)
# Expected Output ​ : 20

# from functools import reduce

# def sum_num(x, y):
#     return x + y

# lst = [8, 2, 3, 0, 7]

# result = reduce(sum_num, lst)
# print(result)

def find_max(L):
    return max(L)

L = [10,12,15,20,13]

print (find_max(L))