import os
from typing import List, Dict
import csv
import dotenv
import pymysql
import os

from pymysql.cursors import Cursor
from dotenv import load_dotenv

__all__ = ['main_menu', 'products_menu', 'couriers_menu', 'orders_menu', 
'load_products', 'save_products', 'load_couriers', 'save_couriers', 'load_orders','save_orders',
'add_product','add_courier', 'add_order', 'execute_query','print_products', 'print_couriers', 'print_orders',
'update_product', 'update_courier', 'update_order', 'update_order_status',
'delete_product', 'delete_courier', 'delete_order']

load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")
connection = pymysql.connect(
host,
user,
password,
database
)

def execute_query(sql):
    
    try:
        connection = pymysql.connect(host, user, password, database, autocommit=True)
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        
        # Execute
        cursor.execute(sql)
        rows = cursor.fetchall()
        
        # Close down
        cursor.close()
    finally:
        connection.close()
    
    return rows

# Add products DB
def add_product():
    name = input('Please enter new product name: ')
    price = input('Please enter new product price: ')
    sql = f"insert into products (product_name, price) values('{name}','{price}')"
    execute_query(sql)
    print(f"~~~{name} has been added to the products!~~~")


# Add couriers DB
def add_courier():
    name = input('Please enter new courier name: ')
    phone = input('Please enter new courier phone number: ')[:11]
    sql = f"insert into couriers (courier_name, courier_phone) values('{name}','{phone}')"
    execute_query(sql)
    print(f"~~~{name} has been added as a courier!~~~")


def add_order():
    customer_name = input("Enter Name: ")
    customer_address = input("Enter Address: ")
    customer_phone = input("Enter Phone Number: ")[:11]
    print_products()
    items = input("Please select a product by its Product ID: ")
    print_couriers()
    courier_id = int(input("Please select a courier by their Courier ID: "))
    status = 'Preparing'
    sql = f'''insert into orders (customer_name, customer_address, customer_phone, products_id, couriers_id, order_status) 
        values ('{customer_name}', '{customer_address}', '{customer_phone}', '{items}', '{courier_id}', '{status}')'''
    execute_query(sql)
    print("~~~Your order has been added!~~~")


def print_products(): 
    sql = "SELECT * FROM products"
    columns = execute_query(sql) 
    for column in columns: 
        print(f"Product ID: {column['product_id']} | {column['product_name']} | £{column['price']}")

def print_couriers(): 
    sql = "SELECT * FROM couriers"
    columns = execute_query(sql) 
    for column in columns: 
        print(f"Courier ID: {column['courier_id']} | {column['courier_name']} | {column['courier_phone']}")

def print_orders():
    sql = "SELECT * FROM orders"
    columns = execute_query(sql)
    for column in columns: 
        print(f"Order ID: {column['order_id']} | {column['customer_name']} | {column['customer_address']} | {column['customer_phone']} | {column['products_id']} | {column['couriers_id']} | {column['order_status']}")


def update_product():
    print_products()
    id = int(input("Please enter Product ID of item you wish to update: "))
    name = input("Please enter updated name: ")
    price = float(input("Please enter updated price: "))
    sql = f"UPDATE products SET product_name = '{name}', price = '{price}' WHERE product_id = '{id}'"
    execute_query(sql)
    print("~~~You have successfully updated this product!~~~")

def update_courier():
    print_couriers()
    id = int(input("Please enter Courier ID of courier you wish to update: "))
    name = input("Please enter new name: ")
    phone = input('Please enter new courier phone number: ')[:11]
    sql = f"UPDATE couriers SET courier_name = '{name}', courier_phone = '{phone}' WHERE courier_id = '{id}'"
    execute_query(sql)
    print("~~~You have successfully updated this courier!~~~")

def update_order():
    print_orders()
    id = int(input("Please enter Order ID of order you wish to update: "))
    name = input("Please enter new name: ")
    address = input("Please enter updated address: ")
    phone = input("Please enter new phone number: ")[:11]
    print_products()
    items = input("Please select a product by its Product ID: ")
    print_couriers()
    courier_id = int(input("Please select a courier by their Courier ID: "))
    status = 'Preparing'
    sql = f"""UPDATE orders SET customer_name = '{name}', customer_address = '{address}', customer_phone = '{phone}'
    , products_id = '{items}', couriers_id = '{courier_id}', order_status = '{status}' WHERE order_id = '{id}'"""
    execute_query(sql)
    print("~~~You have successfully updated this order!~~~")

def update_order_status():
    print_orders()
    id = int(input("Please enter Order ID of order status you wish to update: "))
    print("""---ORDER STATUS OPTIONS---
    1. Preparing
    2. Delivering
    3. Completed
    """)
    new_order_status = int(input("Please enter a number corresponding to new status: "))
    if new_order_status == 1:
        status = 'Preparing'
        sql = f"UPDATE orders SET order_status = '{status}' WHERE order_id = {id}"
        execute_query(sql)
        print("~~~You have successfully updated this order status to PREPARING!~~~")
    elif new_order_status == 2:
        status = 'Delivering'
        sql = f"UPDATE orders SET order_status = '{status}' WHERE order_id = {id}"
        execute_query(sql)
        print("~~~You have successfully updated this order status to DELIVERING!~~~")
    elif new_order_status == 3:
        status = 'Completed'
        sql = f"UPDATE orders SET order_status = '{status}' WHERE order_id = {id}"
        execute_query(sql)
        print("~~~You have successfully updated this order status to COMPLETED!~~~")


def delete_product():
    print_products()
    id = int(input("Please enter Product ID of product you wish to delete: "))
    sql = f"DELETE FROM products WHERE product_id = '{id}'"
    execute_query(sql)
    print("~~~Your product has been deleted!~~~")

def delete_courier():
    print_couriers()
    id = int(input("Please enter Courier ID of courier you wish to delete: "))
    sql = f"DELETE FROM couriers WHERE courier_id = '{id}'"
    execute_query(sql)
    print("~~~This courier has been deleted!~~~")

def delete_order():
    print_orders()
    id = int(input("Please enter Order ID of order you wish to delete: "))
    sql = f"DELETE FROM orders WHERE order_id = '{id}'"
    execute_query(sql)
    print("~~~Your order has been deleted!~~~")


main_menu = '''
-MAIN MENU-
################
0. Exit
1. Products Menu
2. Couriers Menu
3. Order Menu'''

products_menu = '''
-PRODUCTS MENU-
#######################
0. Return To Main Menu
1. Display Product list 
2. Create New Product
3. Update Product
4. Delete Product
'''
couriers_menu = '''
-COURIERS MENU-
#######################
0. Return To Main Menu
1. Display Courier List
2. Add New Courier
3. Update Courier
4. Delete Courier
'''

orders_menu = '''
-ORDERS MENU-
#######################
0. Return To Main Menu
1. Display Orders list
2. Add New Order
3. Update Order Status
4. Update an Order
5. Delete an Order
'''


def load_products(products: List[dict]):
    try:
        with open("products.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                products.append(row)
    except Exception as e:
        print("No file loaded")
    return products

def save_products(products: List[dict]):
    with open("products.csv", "w", newline='') as file:
        field_names = ["product_name","price"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for product in products:
            writer.writerow(product)
    return products

def load_couriers(couriers: List[Dict]):
    couriers = []
    try:
        with open("couriers.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                couriers.append(row)
    except Exception as e:
        print("No file loaded")
    return couriers

def save_couriers(couriers: List[dict]):
    with open("couriers.csv", "w", newline='') as file:
        field_names = ["courier_name","courier_phone"]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for courier in couriers:
            writer.writerow(courier)
    return couriers


def load_orders(orders: List[dict]) -> None:
    orders = []
    try:
        with open("orders.csv", "r") as file:
            csv_file = csv.DictReader(file)
            for row in csv_file:
                orders.append(row)
    except Exception as e:
        print("No file loaded")
    return orders

def save_orders(orders: List[dict]):
    with open("orders.csv", "w", newline='') as file:
        field_names = ["customer_name", "customer_address","customer_phone", "chosen_products", "chosen_courier",'order_status']
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        # instruct the writer to write the row
        for order in orders:
            writer.writerow(order)
    return orders

# Load environment variables from .env file