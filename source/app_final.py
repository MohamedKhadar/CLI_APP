from app_functions import *
import csv
from typing import List, Dict
import dotenv
import pymysql
import os
from pymysql.cursors import Cursor
from dotenv import load_dotenv

# products_list = load_products([])
# couriers_list = load_couriers([])
# orders_list = load_orders([])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Start 
print("Welcome!")
while(True):
    print(main_menu)
    main_menu_options = int(input("Please enter a number: "))
    if (main_menu_options == 0):
        # save_products(products_list)
        # save_couriers(couriers_list)
        # save_orders(orders_list)
        print("Goodbye!")
        break
    elif main_menu_options == 1:
    # product menu
        clear_screen()
        while(True):
            print(products_menu)
            products_menu_options = int(input("Please enter a number: "))
            if products_menu_options == 0:
                print("Back to main menu!")
                clear_screen()
                break
            elif products_menu_options == 1:
                # Print current products
                clear_screen()
                print("These are the current products: ")
                print_products()
            elif products_menu_options == 2:
                #Add new product
                clear_screen()
                add_product()
            elif products_menu_options == 3:
                # STRETCH Updating existing product
                clear_screen()
                update_product()
            elif products_menu_options == 4:
                # STRETCH Deleting existing product
                clear_screen()
                delete_product()
    elif main_menu_options == 2:
        # couriers menu
        clear_screen()
        while(True):
            print(couriers_menu)
            couriers_menu_options = int(input("Please enter a number: "))
            if couriers_menu_options == 0:
                print("Back to main menu!")
                clear_screen()
                break
            elif couriers_menu_options == 1:
                # Print current couriers
                clear_screen() 
                print("These are the current couriers: ")
                print_couriers()
            elif couriers_menu_options == 2:
                #Add new courier
                clear_screen()
                add_courier()
            elif couriers_menu_options == 3:
                # STRETCH Updating existing courier
                clear_screen()
                update_courier()
            elif couriers_menu_options == 4:
                # STRETCH Deleting existing courier
                clear_screen()
                delete_courier()
    elif main_menu_options == 3:
        clear_screen()
        #Orders Menu
        while(True):
            print(orders_menu)
            orders_menu_options = int(input("Please enter a number: "))
            if orders_menu_options == 0:
                print("Back to main menu!")
                clear_screen()
                break
            elif orders_menu_options == 1:
                # Print current orders
                clear_screen()
                print("These are the current orders: ")
                print_orders()
            elif orders_menu_options == 2:
                # Get input for new orders
                clear_screen()
                add_order()
            elif orders_menu_options == 3:
                # Update status of existing order
                clear_screen()
                update_order_status()
            elif orders_menu_options == 4:
                # STRETCH Update existing order
                clear_screen()
                update_order()
            elif orders_menu_options == 5:
                # STRETCH Delete exisiting order
                clear_screen()
                delete_order()
