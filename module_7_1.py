from pprint import pprint

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
    def get_products(self):
        file_ = open(self.__file_name, 'r')
        data_ = file_.read()
        file_.close()
        return data_
    def add(self, *products):
        file_ = open(self.__file_name, 'a')
        for elem_ in products:
            if elem_.name not in self.get_products():
                file_.write(f'{elem_} \n')
            else:
                print(f'Продукт {elem_.name} уже есть в магазине')
        file_.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
