from argparse import ArgumentParser as prsr
from tabulate import tabulate
parser = prsr()
parser.add_argument('--file', type=str, default=None, help='path to file')
parser.add_argument('--where', type=str, default=None, help='filter')
parser.add_argument('--aggregate', type=str, default=None, help='aggregate')

class Product:
    def __init__(self, name, brand, price, rating):
        self.product_dict = {'name': name, 'brand': brand, 'price': price, 'rating': rating.strip()}

class ProductsList:
    def __init__(self):
        self.products_list = []

    def loader(self, execute_path):
        with open(execute_path, 'r') as file:
            for product in file:
                name, brand, price, rating = product.split(',')
                self.products_list.append(Product(name, brand, price, rating))
        self.products_list.pop(0)
    
    def render_where(self, result_list):
        data = []
        for product in result_list:
            line = []
            for value in product.product_dict.values():
                line += [value]
            data.append(line)
        table = tabulate(data, tablefmt="fancy_grid", headers=['name', 'brand', 'price', 'rating'])
        print(table)

    def render_aggregate(self, result_list):
        table = tabulate([[result_list[1]]], tablefmt="fancy_grid", headers=[result_list[0]])
        print(table)

    def get_where(self, where):
        try:
            result_list = []
            if '=' in where:
                key, value = where.split('=')
                for product in self.products_list:
                    if product.product_dict[key] == value:
                        result_list.append(product)
            elif '>' in where:
                key, value = where.split('>')
                for product in self.products_list:
                    if float(product.product_dict[key]) > float(value):
                        result_list.append(product)
            elif '<' in where:
                key, value = where.split('<')
                for product in self.products_list:
                    if float(product.product_dict[key]) < float(value):
                        result_list.append(product)
            return result_list
        except:
            print('Invalid value')

    def get_aggregate(self, aggregate, result_list):
        key, value = aggregate.split('=')
        try:
            if value == 'max':
                result_value = max(float(value.product_dict[key]) for value in result_list)
            elif value == 'min':
                result_value = min(float(value.product_dict[key]) for value in result_list)
            elif value == 'avg':
                result_value = sum(float(value.product_dict[key]) for value in result_list) / len(result_list)
            result_list = [value, result_value]
            self.render_aggregate(result_list)
            return result_list
        except:
            print('Invalid value')

    def execute(self, where=None, aggregate=None):
        if where is not None:
            result_list = self.get_where(where)
        else:
            result_list = self.products_list
        if aggregate is not None:
            result_list = self.get_aggregate(aggregate, result_list)    
        else:
            self.render_where(result_list)
        return result_list