for i in range (0, 101):
    print('The number "i" is equal:', i)
    answer = input('Should we break? ')
    if answer == 'no':
        continue
    elif answer == 'yes':
        print('OK. The cycle completed.')
        break
    else:
        print("Don't understand you.")