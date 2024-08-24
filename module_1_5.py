immutable_var = (17, 'January', True, ['100 rub', '1 dollar', '5 euro'])
print(immutable_var)
print()
print('Попытайтесь изменить элемент кортежа immutable_var.')
print('Введите любое число')
x = input()
print(f'Вы пытаетесь присвоить элементу кортежа immutable_var[0] значение {x}')
print(f'immutable_var[0] = {x}')
print('Проверим результат. \nimmutable_var: ', immutable_var)
print('Как видите, объект типа кортеж является статическим, а не динамическим, в связи с чем изменить содержащиеся в нем элементы не представляется возможным.')
print()
mutable_list = [17, 'January', True, ['100 rub', '1 dollar', '5 euro']]
mutable_list[0] = 16
print(mutable_list)