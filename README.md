# Python Basics Project

## Introduction

In this project, you **learned** the fundamental concepts of Python, including variables, functions, built-ins, packing, unpacking, and exception handling.

## Module: `product_handler`

### Function: `get_product_by_id`

**Parameters:**
- An integer representing the ID of the product to be searched.

**Procedure:**
- If the product with the specified ID **was found** in the menu, **you returned** the dictionary representing it.
- If the product with the specified ID **was not found** in the menu, **you returned** an empty dictionary.

### Function: `get_products_by_type`

**Parameters:**
- A string representing the type of products to be searched.

**Procedure:**
- If no products of the specified type **were found**, **you returned** an empty list.
- If products **were found**, **you returned** a list containing all products of the specified type.

### Function: `add_product`

**Module:** `product_handler`

**Procedure:**
- **You added** this function to the `product_handler` module.
- **You considered** that the product information to be added **was always correct**.
- Parameters:
  - Variable `menu`: A list representing the menu to which the product **should be added**.
  - An indefinite number of named arguments representing the product **to be added**.
- **You generated** a new unique ID for the added product. The new unique ID **was stored** in the "_id" key of the new product, and it **was based** on the highest product ID in the menu, incremented by 1. If there **were no products** in the menu, the generated ID **was 1**.
- After **generating and attaching** the ID to the product, **you added** the product to the menu and **returned** only the added product with the generated ID.

## Module: `tab_handler`

### Function: `calculate_tab`

**Procedure:**
- Initially, **you created** a `tab_handler` module within the `management` package. Your `calculate_tab` function **was in** this new module.
- For educational purposes, **you assumed** that invalid product IDs **would never be passed**.
- Parameters:
  - A list of dictionaries representing the consumption of a table. Each dictionary **contained** the identification ("_id") of the consumed product and the quantity ("amount") of the product consumed.
- **You calculated** the subtotal of the table's consumption and **returned** a dictionary in the specified format, with the "subtotal" key **as a string** and the value **as a float rounded** to a maximum of two decimal places.

## Examples

**You used** the `main.py` file to verify the functionality through prints matching the examples provided. **You didn't focus** on the indentation of the returns; **you formatted** it for readability.

## Refactoring

### Refactoring `get_product_by_id`

**You refactored** your `get_product_by_id` function so that if the passed parameter **was not of type integer**, a `TypeError` exception **was raised** with the message: "product id must be an int."

### Refactoring `get_products_by_type`

**You refactored** your `get_products_by_type` function so that if the passed parameter **was not of type string**, a `TypeError` exception **was raised** with the message: "product type must be a str."

## Additional Task: `report`

**You added** a function to the `product_handler` module to provide a report on some menu data.

### Function: `menu_report`

**Parameters:**
- This function **did not receive** any parameters.

**Procedure:**
- **You compiled** a report on some characteristics of the product menu:
  - Product Count: The total count of products in the menu.
  - Average Price: The average price of all products in the menu, **rounded** to a maximum of 2 decimal places.
  - Most Common Type: The most common product type, i.e., the type that contains the highest quantity of products in the menu.
- The return **was** a formatted string exactly as shown in the example below, with the respective dynamic values:

```plaintext
Product Count: [Count]
Average Price: [Average Price]
Most Common Type: [Most Common Type]
