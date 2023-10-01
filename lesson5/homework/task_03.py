def generate_squares(*args):
    sqr = [i ** 2 for i in args]
    return sqr
print(generate_squares(1, 2, 3))