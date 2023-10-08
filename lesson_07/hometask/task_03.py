# Решите прошлую задачу, в которой теперь пользователь может вводить буквы
# в любом регистре. Вам по прежнему нужно удалить все гласные.
# При этом вывести результат нужно вывести сохранив изначальный регистр.

text = list(input('Введите произвольное количество латинских букв через пробел: '))
def remove_vowels(a: list[str]) -> list[str]:
    return a[0].lower() in 'aeiouAEIOU'

filtred_text = filter(remove_vowels, text)
print(list(filtred_text))
