# Create a list of tuples of first name, last name, and age for your
# friends and colleagues. If you don't know the age, put in None.
# Calculate the average age, skipping over any None values. Print out
# each name, followed by old or young if they are above or below the
# average age.

lst = [
    ('Bipin', 'Ayer', 10),
    ('Dikshya', 'Bimali', None),
    ('Joshna', 'Lama', 25),
    ('Kiran', 'Bhandari', 19),
    ('Shrisanth', 'Ojha', 13),
    ('Sujan', 'Ayer', None),
    ('Subodh', 'Chaudhary', 25),
    ('Sophiya', 'Maharjan', 26),
    ('Alisha', 'Sitaula', None)
]

sum = 0
for item in lst:
    if item[2] == None:
        pass
    else:
        sum += item[2]

average = sum/len(lst)
print('average:', average)

for item in lst:
    if item[2] == None:
        print(item[0], 'Unknown')
    else:
        if item[2] > average:
            print(item[0], 'old')
        else:
            print(item[0], 'young')