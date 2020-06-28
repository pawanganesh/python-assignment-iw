# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

str1 = 'abc'
str2 = 'xyz'


new_str1 = str2[:2]+str1[2:]
new_str2 = str1[:2]+str2[2:]
result = new_str1 + ' ' + new_str2
print(result)