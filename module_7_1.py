from pprint import pprint

class Product:

    def __init__(self, name=str, weight=float, category=str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def add(self, *products):
        self.products = products
        file = open(self.__file_name, 'r+')
        file.tell()
        a = str(file.read())
        file.seek(0)

        for i in range(0,len(products)):
            if a.find(str(self.products[i]))<0:
                file.write(str(self.products[i])+'\n')
            else:
                name_ = str(products[i])
                file.write(f'продукт {name_[:name_.find(','):]} есть в магазине\n')

        file.write(a)
        file.close()


    def get_products(self):
        file=open(self.__file_name, 'r')
        text_ = str(file.read())
        file.close()
        return text_

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())