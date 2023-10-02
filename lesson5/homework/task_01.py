def is_year_leap(year: int):
    if ((year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
        return True
    else:
        return False

assert is_year_leap(2000)

