my_car = {
    "year": 1964,
    "brand": "Ford",
    "model": "Mustang"
}

# print(my_car['brand'])


my_dict = {'key1': 123, 'key2': [12, 23, 33],
           'key3': ['item0', 'item1', 'item2']}


# print(my_dict['key2'])
# print(my_dict['key3'][0])
# print(my_dict['key3'][0].upper())


dict = {'key1': 1, 'key2': 2, 'key3': 3}
# print(dict.keys())
# o/p => dict_keys(['key1', 'key2', 'key3'])

# print(dict.values())
# o/p => dict_values([1, 2, 3])


dict = {'key': 'value'}

d2 = {
    'k1':
    [
        {'nest_key':
            ['this is deep', ['hello']]
         }
    ]
}


# print(d2['k1'][0]['nest_key'][1][0])
