# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(str1):
    if str1 == str1[::-1]:
        print('Palindrome')
    else:
        print("Not palindrome")

word = input("Enter any word:")
is_palindrome(word)
