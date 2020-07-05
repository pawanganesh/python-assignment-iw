# Write code that will print out the anagram (words that use the same
# letters) from a paragraph of text.

paragraph = "cat dog tac god act"
strings = paragraph.split(' ')

anagram = {}
for string in strings:
    key = "".join(sorted(string))
    if string in anagram.keys():
       anagram[key].append(string)
    else:
        anagram[key] = []
        anagram[key].append(string)
result = ""
for key, value in anagram.items():
   result += " ".join(value) + " "
print(result)