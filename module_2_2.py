first, second, third = [int(input('Введите целое число: ')) for _ in range(3)]
if first == second and  third == second:
    print(3)
elif first == second or first == third or third == second:
    print(2)
else:
    print(0)