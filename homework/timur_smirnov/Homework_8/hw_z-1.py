import random

salary = int(input("Введите зарплату: "))
flag = False
bonus_input = input("Если бонус доступен, введите yes': ").lower()
if bonus_input in ["yes", "да", '1']:
    flag = True
if flag:
    bonus_amount = random.randint(5, 20) / 100 * salary
    salary_bonus = salary + bonus_amount
else:
    salary_bonus = salary
print(f"{salary}, {flag} - '${int(salary_bonus)}'")
