def test_function():
    flag = "Функция inner_function выведена в глобальное пространство имен во избежание ошибки."
    global inner_function
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()
    return flag
final_word = test_function()
inner_function()
print(final_word)