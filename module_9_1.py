def apply_all_func(int_list: list, *functions):
    glossia = {}
    for func in functions:
        glossia[func.__name__] = func(int_list)
    return glossia

if __name__ == '__main__':
    print(apply_all_func([6, 20, 15, 9], max, min))
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
