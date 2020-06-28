# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.
# Sample List : ['abc', 'xyz', 'aba', '1221']['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

lst = ['abc', 'xyz', 'aba', '1221']

counter = 0

for word in lst:
    if len(word) >= 2 and word[0] == word[-1]:
            counter += 1

print(counter)
