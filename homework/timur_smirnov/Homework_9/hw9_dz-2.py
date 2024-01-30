temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27,
                22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]
# Создаем список с температурами выше 28 градусов
hot_days = [i for i in temperatures if i > 28]
# Находим самую высокую и самую низкую температуру и вычисляем среднюю
max_temp = max(hot_days)
min_temp = min(hot_days)
average_temp = sum(hot_days) / len(hot_days)
print("Самая высокая температура:", max_temp)
print("Самая низкая температура:", min_temp)
print("Средняя температура:", average_temp)
