import re
from datetime import datetime, timedelta

# Функция для парсинга даты и выполнения действия
def process_date(number, date_obj):
    # Преобразование строки в объект datetime
 
    if number == '1':
        # Добавить неделю к дате
        new_date_obj = date_obj + timedelta(weeks=1)
        return new_date_obj
    elif number == '2':
        # Получить день недели
        return date_obj.strftime('%A')
    elif number == '3':
        # Вычислить количество дней назад от сегодняшнего дня
        days_ago = (datetime.now() - date_obj).days
        return days_ago

# Чтение данных из файла и вызов функции process_date
def process_file_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            matchdate = re.search("(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2}):(\d{2}).(\d{6})", line)
            matchnumber = re.search("^(\d)", line)
            inputdate = datetime.strptime(matchdate[0], '%Y-%m-%d %H:%M:%S.%f') 
            print(process_date(matchnumber[0], inputdate))

# Вызов функции для чтения данных файла
process_file_data('homework/eugene_okulik/hw_13/data.txt')