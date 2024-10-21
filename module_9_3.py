from module_9_2 import second_result

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(el_1) - len(el_2) for el_1, el_2 in zip(first, second) if len(el_1) != len(el_2))
second_result = (len(first[i]) == len(second[i]) for i in range(3))

if __name__ == '__main__':
    print(list(first_result))
    print(list(second_result))