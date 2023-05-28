from datetime import datetime


def saved(name, text):
    name = '|' + name + '|' + ' время создания: ' + str(datetime.now()) + ' ->'
    with open('jotter.txt', 'a', encoding='utf-8') as data:
        print(name, text, file=data)
