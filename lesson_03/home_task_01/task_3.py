vklad = int(input('Введите размер вклада в рублях: '))
year = int(input('Введите количество лет:'))
i = vklad * (1 + 1 / 10) ** year
print('Конечная сумма на счету будет составлять: ' + str(i))