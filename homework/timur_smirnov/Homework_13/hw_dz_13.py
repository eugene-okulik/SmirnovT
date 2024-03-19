import re
from datetime import datetime, timedelta


def process_date(number, date_obj):
    """
    Функция для парсинга даты и выполнения действия.
    """
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


def process_file_data(filename):
    """
    Чтение данных из файла и вызов функции process_date.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            matchdate = re.search(r"(\d{4})\-(\d{2})\-(\d{2}) (\d{2}):(\d{2}):(\d{2}).(\d{6})", line)
            matchnumber = re.search(r"^(\d)", line)
            inputdate = datetime.strptime(matchdate[0], '%Y-%m-%d %H:%M:%S.%f')
            print(process_date(matchnumber[0], inputdate))


# Вызов функции для чтения данных файла
process_file_data('homework/eugene_okulik/hw_13/data.txt')