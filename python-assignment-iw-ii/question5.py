# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.

my_info = 'Pawanlal', 'Ganesh', 20
print(my_info)

people = []

people.append(my_info)
print(people)

my_friend1 = 'Bipin', 'Ayer', 22
people.append(my_friend1)

my_friend2 = 'Shrisanth', 'Ojha', 23
people.append(my_friend2)

my_friend3 = 'Pujan', 'Pradhan', 21
people.append(my_friend3)

print(people)

people.sort()
print('default sort:', people)

people.sort(key= lambda x: x[0])
print('sort by first name:',people)

people.sort(key= lambda x: x[1])
print('sort by last name:',people)

people.sort(key= lambda x: x[2])
print('sort by age:',people)

