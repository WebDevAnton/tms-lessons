n = int(input('Ввeдите число: '))
def generate_natural_cubes(n):
    if n > 0:
        print([i ** 3 for i in range(n + 1)])
    else:
        print('Введите натуральное число. ')
generate_natural_cubes(n)