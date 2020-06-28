# Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'


x = input('Enter a string: ')
if len(x)>=3:
    if x[-3:] == 'ing':
        x += 'ly'
        print(x)
    else:
        x += 'ing'
        print(x)
else:
    print(x)