def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Функция для получения n-го числа Фибоначчи из генератора
def get_fibonacci_number(n):
    fib_gen = fibonacci_generator()
    fib_number = None
    for i in range(n):
        fib_number = next(fib_gen)
    return fib_number

# Распечатать пятое, двухсотое, тысячное и стотысячное число Фибоначчи
print(get_fibonacci_number(5))       # Пятое число
print(get_fibonacci_number(200))     # Двухсотое число
print(get_fibonacci_number(1000))    # Тысячное число
# Стотысячное число займет очень много времени для генерации и может быть вычислено не во всех средах
#print(get_fibonacci_number(100000))  # Стотысячное число