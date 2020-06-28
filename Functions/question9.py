# Write a Python function that takes a number as a parameter and check the
# number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that
# has no positive divisors other than 1 and itself.


def prime_checker(num):
    for i in range(2, num):
        if (num % i) == 0:
            print(num,'is not prime number')
            break
    else:
        print(num, 'is prime number')

prime_checker(4)