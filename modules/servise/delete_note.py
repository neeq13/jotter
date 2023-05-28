from main import start
from modules.commands.all import All
from modules.servise.clear import clear
from modules.servise.search import search


def delete():
    All().execute()
    try:
        num = int(input('Введите номер заметки который хотите удалить: '))
    except:
        clear()
        return print('---> Водите только цифры\n')
    line = search(num)
    if line == -1:
        clear()
        print('---> Такой заметки не сущетсвует\n')
        start()

    with open('jotter.txt', 'r', encoding='utf-8') as data:
        old_data = data.read()

    new_data = old_data.replace(line, '')

    with open('jotter.txt', 'w', encoding='utf-8') as data:
        data.write(new_data)

    clear()
    print('---> Удаление произошло успешно')
    print()
