# Write a Python program to find the length of a tuple


tupl = ('Python', 'is', 'fun', 'to', 'learn', 'and', 'it\'s', 'awesome', 'language')

# print(len(tupl))

length = 0
for _ in tupl:
    length += 1

print(length)