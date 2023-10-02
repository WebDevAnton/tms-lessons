# Напишите функцию get_longest_word,
# которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста.
# Для разбиения строки на слова используйте функцию split.

def get_longest_word(text):
    word = text.split()
    return max(word, key=len)

# Для ознакомления и на будущее
# def get_longest_word(text):
#     longest_word = ''
#     for word in text.split():
#         if len(longest_word) < len(word):
#             longest_word = word
#     return longest_word