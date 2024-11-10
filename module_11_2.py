def introspection_info(obj):
    glossia_obj = {}
    attributes, methods = [], []
    glossia_obj['type'] = obj.__class__.__name__ # Определяем тип объекта.
    for attribute in dir(obj): # Проходим по списку атрибутов и методов, фильтруя их с помощью callable
                               # (определяем свойство вызываемости, присущее функциям / методам объекта).
        if callable(getattr(obj, attribute)):
            methods.append(attribute)
        else:
            attributes.append(attribute)
    glossia_obj['attributes'] = attributes
    glossia_obj['methods'] = methods
    glossia_obj['module'] = obj.__class__.__module__ # Определяем модуль объекта с помощью встроенного атрибута.
    glossia_obj['id'] = id(obj) # Выясняем айди объекта в памяти.
    return glossia_obj

class Fury(): # Объявляем пользовательский класс.
    def __init__(self, paws: int, tail: bool):
        self.paws = paws
        self.tail = tail
    def clock(self):
        print('Bow!')

if __name__ == '__main__':
    quadrober = Fury(4, True)
    number_info = introspection_info(quadrober)
    print(number_info)
