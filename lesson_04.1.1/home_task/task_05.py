number = int(input('Введите произвольное число: '))
if number > 0:
    result_1 = number % 10
    result_2 = number // 10
    result_3 = result_1 + result_2
    print('Сумма цифр числа', number, 'равна: ', result_3)
else:
    print('Ошибка. Введите число, которое больше 0')


