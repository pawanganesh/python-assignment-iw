# Write a Python function to check whether a number is in a given range.


def num_range(num):
    if num in range(20, 30):
        print(num, 'is in the range')
    else:
        print(num,'is outside of the range')

num = int(input('Enter an integer: '))
num_range(num)