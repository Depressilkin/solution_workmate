from model import Product, ProductsList

product = Product('iphone 15 pro', 'apple', '999', '4.9')
other_product = Product('galaxy s', 'samsung', '900', '4.0')
products_list = ProductsList()
products_list.products_list = [product, other_product]
    
def test_init_product():
    assert product.product_dict ==  {'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'}

def test_get_where():
    assert products_list.get_where('brand=apple') == [product]
    assert products_list.get_where('brand=samsung') == [other_product]
    assert products_list.get_where('price>950') == [product]
    assert products_list.get_where('price<950') == [other_product]

def test_get_aggregate():
    assert products_list.get_aggregate('rating=max', [product, other_product]) == ['max', 4.9]
    assert products_list.get_aggregate('rating=min', [product, other_product]) == ['min', 4.0]
    assert products_list.get_aggregate('rating=avg', [product, other_product]) == ['avg', 4.45]

def test_execute():
    assert products_list.execute() == [product, other_product]
    assert products_list.execute(where='price>950') == [product]
    assert products_list.execute(where='price>950', aggregate='rating=max') == ['max', 4.9]