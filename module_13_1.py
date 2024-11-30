# Импортируем модуль асинхронности.
import asyncio

# Создаем первую асинхронную функцию для силача.
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    # Создаем переменную, в которую записываем время задержки - 10 секунд, деленные на силу силача.
    pause_time = 10 / power
    # Основная часть функции, в которой силач поднимает шары. С применением задержки согласно ранее определенной переменной.
    for num_ball in range(1, 6):
        await asyncio.sleep(pause_time)
        print(f'Силач {name} поднял {num_ball} шара')
    print(f'Силач {name} закончил соревнования.')

# Создаем вторую асинхронную функцию, принимающую список силачей.
async def start_tournament(arguments: list):
    # Создаем промежуточный словарь, в котором будут помещаться таски.
    glossia = {}
    # Инициализируем таски, пробежавшись по ним циклом фор.
    for i in range(len(arguments)):
        glossia[f'task_{i}'] = asyncio.create_task(start_strongman(arguments[i][0], arguments[i][1]))
    # Выставляем эвейты-заглушки, чтобы таски работали корректно / одновременно.
    for i in range(len(arguments)):
        await glossia[f'task_{i}']

if __name__ == '__main__':
    # Создаем список силачей для турнира.
    lib = [('Hercules', 5), ('Hector', 3), ('Ahilles', 4)]
    # Запускаем турнир командой ран.
    asyncio.run(start_tournament(lib))