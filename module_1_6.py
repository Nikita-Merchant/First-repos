my_dict = {'Nikita': 911601, 'Elena': 641409, 'Tamara': 412811}
print(my_dict)
print(my_dict['Nikita'])
print(my_dict.get('Misha'))
my_dict.update({'Misha' : 880505, 'Sergey': 751606})
x = my_dict.pop('Tamara')
print(x)
print(my_dict)
print()
my_set = {16, 17, '0505', '1601', 2, 12, 16, 17, True, 17, '0505'}
print(my_set)
set_2 = {False, 'Nikita'}
my_set = my_set.union(set_2)
my_set.discard(17)
print(my_set)