# Write a Python function to insert a string in the middle of a string.

# Sample function and result :

# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}


def insert_string_middle(str1, str2):
    mid_str = len(str1)//2
    result = str1[:mid_str] + str2 + str1[mid_str:]
    print(result)

insert_string_middle('[[]]<<>>','Python')
insert_string_middle('{{}}','PHP')