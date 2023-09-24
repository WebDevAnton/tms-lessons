month = {'January': 31,
         'February': 28,
         'March': 31,
         'April': 30,
         'May': 31,
         'June': 30,
         'July': 31,
         'August': 31,
         'September': 30,
         'October': 31,
         'November': 30,
         'December': 31
}
name = input('Введите название месяца на английском языке:')
day = int(input('Введите число:'))
i = int(month.get(name))
if (day <= i) and (day <= i):
    print("TRUE")
else:
    print("FALSE")