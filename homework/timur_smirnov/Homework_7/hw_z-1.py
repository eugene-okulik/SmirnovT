import random

rand_int = random.randint(1, 100)
print('Угадай двухзначное число загаданное программой.')
while True:
    game_input = input('Твой вариант: ')
    if game_input.isdigit():
        game_int = int(game_input)
        if game_int > rand_int:
            print('Загаданное число меньше... Попробуй еще!')
        elif game_int < rand_int:
            print('Загаданное число больше... Попробуй еще!')
        else:
            print("Ты угадал!")
            break
    else:
        print('Нужно ввести именно положительное целое число.')
        