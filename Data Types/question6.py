# Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

str1 = 'The lyrics is not that poor!'

word = str1.split()

if "not" and "poor!" in word:
    index_of_not = word.index('not')
    index_of_poor = word.index('poor!')
    del word[index_of_not:index_of_poor+1]
    word.append('good!')
    print(word)
    


