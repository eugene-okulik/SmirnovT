def extract_number_and_add(text, add_value):
    number = int(text.split(':')[-1].strip())
    return number + add_value


results = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9"
]
for result in results:
    new_number = extract_number_and_add(result, 10)
    print(new_number)
