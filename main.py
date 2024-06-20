"""
Ideas:
  # Create 
    x def create_id(): to generate ids
    x def add_item(name, price, quantity, description): first read the last id on csv then continue with id + 1, save to csd
  # Read
    x def read(id): print name & price & quantitiy & description
  # Update
    x def update(id): prompt("name: " & "price: " & "quantity: " & "description: "), leave empty to not change
  # Delete
    x def delete(id): delete item from csv
  # Others: 
    def sort_by_price() use quick sort
    def add_to_cart() > add to a list
    def check_out() > show total price, confirm order, show receipt
    def search_item(name/price/id) > use binary search
    def browse_item() > browse 10 item at a time, show name price etc
  
  # Idk:
    class item:
      name > string
      price > integer
      quantity > integer
      description > string
      id > string
"""

import os
import functions as fu

while True:
    print("1. Search Item\n2. Add Item\n3. Update Item\n4. Delete Item\n5. Quit")
    do = input("Please choose from the available options: ")
    fu.clear()
    
    if do == '1':
        identity = input("Item ID: ")
        fu.enterToContinue()
        fu.clear()
        fu.searchItem(identity)
        fu.enterToContinue()
    elif do == '2':
        name = input("Item name: ")
        price = input("Item price: ")
        quantity = input("Item quantity: ")
        description = input("Item description: ")
        fu.addItem(name, price, quantity, description)
        fu.enterToContinue()
    elif do == '3':
        identity = input("Item ID: ")
        new_name = input("New name (leave empty to not change): ")
        new_price = input("New price (leave empty to not change): ")
        new_quantity = input("New quantity (leave empty to not chagne): ")
        new_description = input("New description (leave empty to not change): ")
        fu.enterToContinue()
        fu.clear()
        fu.updateItem(int(identity), new_name, new_price, new_quantity, new_description)
        fu.enterToContinue()
    elif do == '4':
        identity = input("Item ID: ")
        fu.enterToContinue()
        fu.clear()
        fu.deleteItem(int(identity))
        fu.enterToContinue()
    elif do == '5':
        break


