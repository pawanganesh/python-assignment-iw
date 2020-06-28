# Write down a python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

sentence = "google.com"
result = {}

for i in sentence:
  if i in result:
    result[i] += 1
  else:
    result[i] = 1
print(result)