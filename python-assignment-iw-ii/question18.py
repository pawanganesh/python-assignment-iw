# Find a package in the Python standard library for dealing with
# JSON. Import the library module and inspect the attributes of the
# module. Use the help function to learn more about how to use the
# module. Serialize a dictionary mapping 'name' to your name and 'age'
# to your age, to a JSON string. Deserialize the JSON back into
# Python.

import json

# print(dir(json))
# print(help(json))

my_dict = {
    'name': 'Pawanlal Ganesh',
    'age': 20
}

json_str = json.dumps(my_dict)
print(json_str)

dict_obj = json.loads(json_str)
print(dict_obj)