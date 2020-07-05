# Create a list with the names of friends and colleagues. Search for the
# name 'John' using a for a loop. Print 'not found' if you didn't find it.

friends = ["Anil", "Kiran", "Samikshya", "Dikshya", "Denisha", "John"]

for friend in friends:
    if "John" in friend:
        print('Found')
        break
else:
    print("Not found")




# y = ["Anil", "Kiran", "Samikshya", "Dikshya", "Denisha", "John"]
# z = 0
# for x in y:
#     if x == "John":
#         print('Found')
#         break
#     else:
#         z = z + 1
#         if len(y) == z:
#             print("Not Found")




