from management.product_handler import *
from management.tab_handler import *

...
if __name__ == "__main__":

    non_integer_id = "2"
    try:
        print('Aqui ', get_product_by_id(52))
    except TypeError:
        print('product id must be an int')

    non_str_type = 2
    try:
        print(get_products_by_type(non_str_type))
    except TypeError:
        print('product type must be a str')

    print('ultima', menu_report())

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }

    print('aqui adicionei um produto', add_product([], **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]

    print(calculate_tab(table_1))
    print(calculate_tab(table_2))
