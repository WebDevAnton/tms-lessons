year = int(input('введите число: '))
def is_year_leap(year):
    if ((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
        print('TRUE')
        print('False')
is_year_leap(year)

