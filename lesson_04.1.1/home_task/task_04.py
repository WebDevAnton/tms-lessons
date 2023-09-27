import random
n = random.randint(0, 100)
while True:
    a = int(input('Введите число: '))
    if a > n:
        print('Не угадал, число больше загаданного ')
    elif a < n:
        print('Не угадал, число меньше загаданного.')
    else:
        print('Угадал. Победа! ')
        break