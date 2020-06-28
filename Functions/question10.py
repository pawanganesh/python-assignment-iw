# Write a Python program to print the even numbers from a given list.
# Sample List : ​ [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result ​ : [2, 4, 6, 8]

even_lst = []

def even_checker(lst):
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    return even_lst


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_checker(lst))