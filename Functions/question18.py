# Write a Python program to check whether a given string is number or not
# using Lambda.


num_checker = lambda x: print('Number') if x.isnumeric() else print("Not Number")

num_checker("2134")
