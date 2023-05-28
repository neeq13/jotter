from datetime import datetime

from main import start
from modules.commands.all import All
from modules.servise.clear import clear
from modules.servise.search import search


def updated():
    All().execute()
    try:
        num = int(input('Введите номер заметки: '))
    except:
        clear()
        return print('---> Водите только цифры\n')
    line = search(num)

    if line == -1:
        clear()
        print('---> Такой заметки не сущетсвует\n')
        start()

    line_to_split = search(num).split('->')
    name = line_to_split[0]
    text = line_to_split[1]

    print(f'Текущее название заметки:', name[1:line_to_split[0].index('|', 1)])
    temp_name = input('Хотите изменить название заметки?: \n')
    print(f'Текущий текст заметки:', text)
    temp_text = input('Хотите изменить название заметки?: \n')

    if temp_name != '':
        name = '|' + temp_name + '|' + ' время обновления: ' + str(datetime.now()) + ' -> '
    else:
        name = '|' + name[1:line_to_split[0].index('|', 1)] + '|' + ' время обновления: ' + str(datetime.now()) + ' -> '
    if temp_text != '':
        text = name + temp_text
    else:
        text = name + text

    with open('jotter.txt', 'r', encoding='utf-8') as data:
        old_data = data.read()

    new_data = old_data.replace(line, text)

    with open('jotter.txt', 'w', encoding='utf-8') as data:
        data.write(new_data)

    clear()
    print('---> Обновление произошло успешно')
    print()
