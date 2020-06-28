# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.

# Sample String : 'restart'
# Expected Result : 'resta$t'

word = 'restart'
result = ""

for i in range(len(word)):
  if i == 0:
    result += word[0]
  elif word[0] in word[i]:
    result += '$'
  else:
    result += word[i]
print(result)