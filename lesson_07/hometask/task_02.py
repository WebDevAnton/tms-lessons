# Пользователь вводит произвольное количество маленьких латинских букв через пробел.
# Напишите функцию remove_vowels, которая принимает список из этих букв и удаляет из
# него все гласные буквы. Выведите результат работы на экран.

text = list(input('Введите произвольное количество маленьких латинских букв через пробел: '))
def remove_vowels(a: list[str]) -> list[str]:
    return a[0].lower() in 'aeiou'

filtred_text = filter(remove_vowels, text)
print(list(filtred_text))
