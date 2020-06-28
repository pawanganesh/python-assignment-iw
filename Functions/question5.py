# Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.


def factorial(num):
    res = 1
    for i in range(1,num+1):
        res *= i
    return res

print(factorial(5)) 

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial((num - 1))
# print('Factorial:',factorial(5)) 