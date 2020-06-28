# Write a Python program to create Fibonacci series upto n using Lambda.

from functools import reduce

fibonacci = lambda n: reduce(lambda a, b: a+[a[-1]+a[-2]], range(n-2),[0, 1])

print(fibonacci(10))

