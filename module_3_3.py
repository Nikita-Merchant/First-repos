def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(2, 'word', False)
print_params(17, 18)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['16', 'Akella', 'True']
values_dict = {'a': 'Elza', 'b': True, 'c': 721}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [True, 'String']
print_params(*values_list_2, 42)
