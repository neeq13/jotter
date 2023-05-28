from modules.commands.all import All
from modules.commands.close import Close
from modules.commands.delete import Delete
from modules.commands.newnote import NewNote
from modules.commands.update import UpdateNote
from modules.servise.clear import clear

menu_item = [All(), NewNote(), UpdateNote(), Delete(), Close()]


def print_menu():
    text = []
    for item in menu_item:
        text.append(item.description())
    return text


def execute(num):
    try:
        temp = int(num)
    except:
        clear()
        return print('---> Водите только цифры\n')
    item = menu_item[temp - 1]
    item.execute()