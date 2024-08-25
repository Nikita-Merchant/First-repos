my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_1 = 0
while index_1 < len(my_list):
    if my_list[index_1] > 0:
        print(my_list[index_1])
        index_1 += 1
    elif my_list[index_1] == 0:
        index_1 += 1
        continue
    else:
        break
