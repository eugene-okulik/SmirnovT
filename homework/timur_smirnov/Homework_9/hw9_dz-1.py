from datetime import datetime

date_str = "Jan 15, 2023 - 12:05:33"
# Преобразование строки в объект datetime
date = datetime.strptime(date_str, '%b %d, %Y - %H:%M:%S')
# 1. Распечатаем полное название месяца
month_name = date.strftime('%B')
print(month_name)  # January
# 2. Распечатаем дату в формате "15.01.2023, 12:05"
formatted_date = date.strftime('%d.%m.%Y, %H:%M')
print(f'"{formatted_date}"')  # 15.01.2023, 12:05
