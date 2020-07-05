# Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?


lst = ['Shrisanth', 'Bibek', 'Asish', 'Junita']
print('Id of list before append:', id(lst))

friends = ['Kiran', 'Denisha', 'Rajat']
lst.append(friends)

print('lst after append:', lst)

print('Id of list after append', id(lst))

lst.sort()
print('After sort:', lst)

print('First item:', lst[0])
print('Second item:', lst[1])

# Conclusion
# 1. Id did not change
# 2. First Item: ['Kiran', 'Denisha', 'Rajat']
# 3. Second Item: Asish