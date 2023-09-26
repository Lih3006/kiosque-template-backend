import collections
import operator
from typing import Counter
from menu import *


def get_product_by_id(user_id):

    if not isinstance(user_id, int):
        raise TypeError("product id must be an int")
    else:
        for product in products:
            if product['_id'] == user_id:

                return product
            else:
                continue
        return {}


def get_products_by_type(type_product) -> list:
    list_product = []

    if not isinstance(type_product, str):
        raise TypeError("product type must be a str")
    else:
        for product in products:
            if product['type'] == type_product:
                list_product.append(product)
    return list_product


def add_product(menu, **kwargs):
    output_new_product = {}
    if len(menu) == 0:
        _id = 1
    else:
        menu.sort(key=operator.itemgetter('_id'))
        _id = menu[-1].get('_id')+1
    for key, value in kwargs.items():
        output_new_product['_id'] = _id
        output_new_product[key] = value
        menu.append(output_new_product)
    print(menu)
    return output_new_product


def menu_report():
    total_products = len(products)
    type_product = []
    sum_price = 0
    most_common_type = ''
    for product in products:
        for key, value in product.items():
            if key == 'price':
                sum_price = sum_price+value
            if key == 'type':
                type_product.append(value)
    compare_types = Counter(type_product)
    most_common_type = list(compare_types.keys())[0]

    average_price = round(sum_price/total_products, 2)

    result = f"Products Count: {total_products} - Average Price: ${average_price} - Most Common Type: {most_common_type}"

    return result
