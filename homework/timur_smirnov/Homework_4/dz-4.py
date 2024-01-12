my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [1, 2, 3, 4, 5],
    'dict': {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
    'set': {1, 2, 3, 4, 5}
}

# Для кортежа
print(my_dict['tuple'][-1])

# Для списка
my_dict['list'].append(6)
del my_dict['list'][1]

# Для словаря
my_dict['dict']['i am a tuple'] = 'primer'
del my_dict['dict']['b']

# Для множества
my_dict['set'].add(6)
my_dict['set'].discard(1)

# Вывести весь словарь
print(my_dict, end=',')
    