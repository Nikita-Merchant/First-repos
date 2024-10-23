def all_variants(text: str):
    for num_1 in range(len(text)):
        for num_2 in range(num_1, len(text)):
            if num_1 == 0:
                yield text[num_2: num_2 + 1]
            else:
                yield text[num_2-num_1: num_2 + 1]

if __name__ == '__main__':
    a = all_variants("abc")
    for i in a:
        print(i)