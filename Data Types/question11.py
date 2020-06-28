# Write a Python program to count the occurrences of each word in a given
# sentence.

sentence = "The man spent a long time finding the right ingredients \
at the grocery store but was too tired to make dinner after getting \
home from the grocery store"

sentence_lst = sentence.split()
result = {}

for word in sentence_lst:
    if word in result:
        result[word] += 1
    else:
        result[word] = 1

print(result)