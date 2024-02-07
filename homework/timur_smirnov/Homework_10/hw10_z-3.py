def decide_operation(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second and (first >= 0 and second >= 0):
            return func(first, second, '-')
        elif first < second and (first >= 0 and second >= 0):
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
    return wrapper


@decide_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


# Запрос чисел у пользователя
first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

# Вызываем функцию с декоратором
result = calc(first, second)
print("Результат:", result)
