#​ Write a Python program to remove the n​ th​ index character from a nonempty
# string.


str1 = 'Pythonisawesome'
n = 5
first_half = str1[:n]
second_half = str1[n+1:]
result = first_half + second_half
print(result)


