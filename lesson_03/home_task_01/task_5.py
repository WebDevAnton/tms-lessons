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
print('Название месяца:',name, '.', 'Число дней:', month.get(name))