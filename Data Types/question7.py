# Write a Python function that takes a list of words and returns the length of the
# longest one.

lst = ['Python', 'is', 'awesome']
def longest_length(lst):
    length = 0
    for i in lst:
        if len(i) > length:
            length = len(i)
            longest_word = i
    print(longest_word + ': ' + str(length))
longest_length(lst)