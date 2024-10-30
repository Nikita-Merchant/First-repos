from time import monotonic
from multiprocessing.pool import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as data:
        flag = 1
        while flag:
            all_data.append(data.readline())
            if all_data[-1] == '':
                flag = 0

if __name__ == "__main__":
    filenames = [f'./file {number}.txt' for number in range(1, 5)]
    flag = 1
    if flag:
        time_start_1 = monotonic()
        for name_file in filenames:
            read_info(name_file)
        time_end_1 = monotonic()
        time_res_1 = time_end_1 - time_start_1
        print(f'Время работы линейного вызова {time_res_1}.')
        flag = 0

    if flag == 0:
        time_start_2 = monotonic()
        with Pool(4) as pool:
            pool.map(read_info, filenames)
        time_end_2 = monotonic()
        time_res_2 = time_end_2 - time_start_2
        print(f'Время работы многопоточного вызова {time_res_2}.')


