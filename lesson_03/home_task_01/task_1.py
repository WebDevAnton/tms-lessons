a = int(input('Введите значение стороны квадрата:'))
per = 4 * a
sqr = a ** 3
diag = a * (2 ** 0.5)
tuple_a = (per, sqr, diag)
print(str(tuple_a[0]) + ', ' + str(tuple_a[1]) + ', ' + str(tuple_a[2]) + '.')