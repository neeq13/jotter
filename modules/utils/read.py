import os.path


def readed(text):
    if not os.path.exists('jotter.txt'):
        file = open('jotter.txt', 'w+')
        file.close()

    with open('jotter.txt', 'r', encoding='utf-8') as data:
        if text == '':
            count = 1
            result = data.readlines()
            print(f'---> Количество заметок: {len(result)}')
            for line in result:
                print(f'{count}:', end='	')
                for text in line.split("->"):
                    print(text.strip())
                count += 1
            print('--------------')
        else:
            count = 1
            for line in data:
                if count == text:
                    return line
                count += 1
            return -1