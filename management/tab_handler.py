from menu import *


def calculate_tab(kwargs):
    subtotal = {'subtotal': '0'}
    total = 0
    for product in products:
        for table in kwargs:
            for key, value in table.items():
                if key == '_id' and product[key] == value:
                    price = product.get('price')
                    amount = table.get('amount')
                    total = total + price * amount
    total_str = f"${round(total,2)}"
    subtotal['subtotal'] = total_str
    return subtotal
