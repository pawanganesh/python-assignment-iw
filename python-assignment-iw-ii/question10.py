# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.

def converter(str1, separator):
    str2 = str1[0].lower()
    for i in str1[1:]:
        if i.isupper():
            str2 += separator + i.lower()
        else:
            str2 += i.lower()
    print(str2)

camel_str = 'ThisIsCamelCased'
camel_sep = '_'
snake_sep = '-'

converter(camel_str, camel_sep)
converter(camel_str, snake_sep)