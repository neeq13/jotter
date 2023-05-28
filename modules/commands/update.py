from modules.servise.clear import clear
from modules.servise.update_note import updated


class UpdateNote:
    def description(self):
        return 'Редактировать заметку'

    def execute(self):
        clear()
        print('---> Процесс обновления заметки')
        print()
        updated()
