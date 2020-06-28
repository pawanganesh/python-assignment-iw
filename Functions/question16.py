# Write a Python program to square and cube every number in a given list of
# integers using Lambda.

lst = [1, 2, 3, 4, 5]

square = lambda x: x**2
cube = lambda x: x**3

lst_square = list(map(square, lst))
lst_cube = list(map(cube, lst))

print(lst_square)
print(lst_cube)


