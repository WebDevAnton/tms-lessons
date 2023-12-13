# УСЛОВИЯ ДЗ
# 1. Прочитать файлик HW_Files.txt
# 2. Преобразовать его в json, где имя ключ, значение - фамилия
# 3. Записать в файлик json с сортировкой по ключам

import json

dict_homework = {}

with open('HW_Files.txt', 'r', encoding='utf-8') as file:
    lines = file.read().splitlines()

    for line in lines:
        key, value = line.split(',')
        dict_homework[key] = value

with open("HW_F.json", "w", encoding='utf-8') as json_file:
    json.dump(
        dict_homework,
        json_file,
        sort_keys=True,
        ensure_ascii=False,
        indent=4,
    )