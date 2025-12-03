## Write a python program to display all items (both keys and values) of any python dictionary.


## creating a dictionary
my_dict = {
    'name': 'Shyam',
    'age': 15,
    'class': 9
}


## .items() for accessing both keys and values of a dictionary
for key, value in my_dict.items():
    print(key, ":", value)


## .keys() for accessing only keys of a dictionary
for key in my_dict.keys():
    print(key)


## .values() for accessing only values of a dictionary
for value in my_dict.values():
    print(value)


