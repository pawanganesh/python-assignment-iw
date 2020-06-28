# Write a Python program to check whether all dictionaries in a list are empty or
# not.
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False


lst1 = [{},{},{}]
lst2 = [{1, 2}, {}, {}]

def empty_checker(lst):
    for item in lst:
        if len(item) > 0:
            return False
    return True


print(empty_checker(lst1))
print(empty_checker(lst2))