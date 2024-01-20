results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]
for result in results:
    index = result.index(":")
    number_str = result[index + 2:] 
    number = int(number_str) 
    new_number = number + 10
    print(new_number)