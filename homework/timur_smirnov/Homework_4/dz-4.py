my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(6)
del my_dict['list'][1]
my_dict['dict'][('i am a tuple',)] = 'primer'
del my_dict['dict']['b']
my_dict['set'].add(6)
my_dict['set'].discard(1)
print(my_dict)
