from modules import menu


def start():
    count = 1
    while True:
        for item in menu.print_menu():
            print(f'{count}: {item}')
            count += 1
        count = 1
        menu.execute(input('Введите номер пункта меню: '))


if __name__ == '__main__':
    start()
