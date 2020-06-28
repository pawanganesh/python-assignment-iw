# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

# Sample String ​ : 'The quick Brow Fox'
# Expected Output : ​
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


def counter(str1):
    upper_count = 0
    lower_count = 0
    for i in str1:
        if i.isupper():
            upper_count += 1
        else:
            lower_count += 1
    print(upper_count)
    print(lower_count)

counter('PythonIsAwesomeAndFunToLearn')