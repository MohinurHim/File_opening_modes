# Задача "Учёт товаров":
from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self): #  возвращает строку в формате '<название>, <вес>, <категория>'
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt' # Инкапсулированный атрибут
    def  get_products(self):  # считывает всю информацию из файла
        file = open(self.__file_name, 'r')
        product = file.read()
        file.close() # закрывает файл
        return str(product) # возвращает единую строку со всеми товарами из файла
    def add(self, *products): # Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле
        file1 = open(self.__file_name, 'a')
        for element in products:
            if str(element) in self.get_products():
                print(f'Продукт {str(element)}уже есть в магазине')
            else:
                file1.write(str(element) + '\n')
        file1.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
