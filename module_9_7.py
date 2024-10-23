def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        flag = 0
        if result <= 1:
            flag = 1
        for i in range(2, int(result**0.5) + 1):
            if result % i == 0:
                flag = 1
        if flag == 0:
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c


if __name__ == '__main__':
    result = sum_three(2, 3, 6)
    print(result)