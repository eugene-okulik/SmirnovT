PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# Преобразуем строку PRICE_LIST в словарь
price_dict = {line.split()[0]: int(line.split()[1].replace('р', '')) for line in PRICE_LIST.split('\n')}
print(price_dict)
