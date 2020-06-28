# Write a Python function to multiply all the numbers in a list.

# Sample List : ​ (8, 2, 3, -1, 7)
# Expected Output ​ : -336

from functools import reduce

def mul_num(x, y):
    return x*y

lst = [8, 2, 3, -1, 7]
res = reduce(mul_num, lst)
print(res)

# Method - 2
# mul = 1
# for i in lst:
#     mul *= i
# print(mul)


