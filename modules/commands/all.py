from modules.servise.clear import clear
from modules.servise.search import search


class All:
    def description(self):
        return 'Вывести все имеющиеся заметки'

    def execute(self):
        clear()
        search('')

