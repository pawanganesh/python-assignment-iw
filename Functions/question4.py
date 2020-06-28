# Write a Python program to reverse a string.

# Sample String ​ : "1234abcd"
# Expected Output ​ : "dcba4321"

def reverse_string(str1):
    return str1[::-1]

str1 = '1234abcd'

res = reverse_string(str1)
print(res)


# Method - Two
# res = ''
# n = len(str1)
# for i in range(-1, -n-1, -1):
#     res += str1[i]

# print(res)
