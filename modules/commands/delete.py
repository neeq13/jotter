from modules.servise.clear import clear
from modules.servise.delete_note import delete


class Delete:
    def description(self):
        return 'Удалить заметку'

    def execute(self):
        clear()
        print('---> Процесс удаления заметки')
        print()
        delete()

