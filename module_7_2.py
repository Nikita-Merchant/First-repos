from pprint import pprint
def custom_write(file_name: str, strings: list):
    file_ = open(file_name, 'w', encoding='utf-8')
    strings_positions ={}
    for i in range(len(strings)):
        strings_positions[(i+1, file_.tell())] = strings[i]
        file_.write(f'{strings[i]}\n')
    file_.close()
    return strings_positions


if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

