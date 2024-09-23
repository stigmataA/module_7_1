# from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        product_file = open(self.__file_name, 'a')
        product_file.close()


    def get_products(self):
        products_file = open('products.txt', 'r')
        products = products_file.read()
        products_file.close()
        return products

    def add(self, *products):
        #current_products = self.get_products()
        #print(products)
        for i in products:
            if self.get_products().find(f'{i.name},') == -1:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            #elif self.get_products().split('\n')[self.get_products().find(f'{i.name},')][1]!= i.weight:

            else:
                print(f'Продукт {i.name} уже есть в магазине')
            print(self.get_products().split('\n')[self.get_products().find(f'{i.name},')])

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
