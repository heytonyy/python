import re
from store import Store
from product import Product
import random

tonys_store = Store("Tony's Magic Shoppe")

tonys_store.add_product(Product("MANA POTION", 50, "Consumables"))
tonys_store.add_product(Product("HEALTH POTION", 50, "Consumables"))
tonys_store.add_product(Product("GREATER MAGIC WAND", 100, "Weapons"))
tonys_store.add_product(Product("FIREBOLT", 200, "Spells"))
tonys_store.add_product(Product("FROSTBOLT", 100, "Spells"))
tonys_store.add_product(Product("THUNDERBOLT", 150, "Spells"))

og_num_products = len(tonys_store.products)

currently_buying = True

def buying_msg():
    print(" ")
    print(" GREAT! WHAT WOULD YOU LIKE TO BUY? ")
    response = input()
    response = response.upper()
    for item in tonys_store.products:
        if item.name == response:
            print(" ")
            tonys_store.sell_product(item.id)
    if og_num_products == len(tonys_store.products):
        print(" SORRY I CANT UNDERSTAND, COME BACK LATER! ")
        exit()
    print(" ")
    print(" THANK YOU! HERES OUR CURRENT ITEMS ")
    print(" ")
    for item in tonys_store.products:
        item.print_info()
        print("---")


##########

print(" ")
print(" >>> WELCOME TO TONY'S MAGIC SHOP <<< ")
print(" ")
print(" HERE IS A LIST OF ITEMS WE CURRENTLY HAVE: ")
print(" ")
for item in tonys_store.products:
    item.print_info()
    print("---")
print(" ")
while currently_buying:
    print(" WOULD YOU LIKE TO BUY SOMETHING? Y/N?")
    response = input()
    if response.upper() == "N":
        print(" THANKS FOR STOPPING BYE! TAKE CARE ")
        print(" ")
        exit()
    buying_msg()


##########