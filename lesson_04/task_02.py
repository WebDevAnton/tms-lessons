for i in range (0, 101):
    answer = input('Should we break?')
    if answer == 'yes':
        break
    print(i)
print('OK. The cycle was finished')