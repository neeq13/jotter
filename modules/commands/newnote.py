from modules.utils import save
from modules.servise.clear import clear


class NewNote:
    def description(self):
        return 'Добавить новую заметку'

    def execute(self):
        clear()
        print('---> Процесс создания заметки')
        print()
        name = input('Введите название заметки: ')
        text = input('Введите тело заметки: \n')
        save.saved(name, text)
        clear()
        print('---> Новая заметка успешно создана')
        print()
