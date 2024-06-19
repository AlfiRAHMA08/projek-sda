"""
Idea:
  # Create 
    def add_item(name, price, quantity, description): first read the last id on csv then continue with id + 1, save to csd
  # Read
    def read(id): print name & price & quantitiy & description
  # Update
    def update(id): prompt("name: " & "price: " & "quantity: " & "description: "), leave empty to not change
  # Delete
    def delete(id): delete item from csv

  # Others:
    class item:
      name > string
      price > integer
      quantity > integer
      description > string
      id > string
      
    def sort_by_price() use quick sort
    def add_to_cart() > add to list
    def check_out() > show total price, confirm order, show receipt
    def search_item(name/price/id) > use binary search
"""

import csv

class Item:
    def __init__(self, id, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description
        self.id = id

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Description: {self.description} Is successfully added!"

file_path = 'items.csv'

def initialize_csv():
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'price', 'quantity', 'description'])

def read_items():
    items = []
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                items.append(Item(row['id'], row['name'], int(row['price']), int(row['quantity']), row['description']))
    except FileNotFoundError:
        pass
    return items

def save_items(items):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['id', 'name', 'price', 'quantity', 'description'])
        for item in items:
            writer.writerow([item.id, item.name, item.price, item.quantity, item.description])

def add_item(name, price, quantity, description):
    items = read_items()
    if items:
        last_id = int(items[-1].id)
        new_id = last_id + 1
    else:
        new_id = 1

    new_item = Item(new_id, name, price, quantity, description)
    items.append(new_item)
    save_items(items)
    print(f"Item added successfully with ID: {new_id}")

def read_item(id):
    items = read_items()
    for item in items:
        if item.id == id:
            print(item)
            return
    print(f"Item with ID {id} not found")

def update_item(id, name=None, price=None, quantity=None, description=None):
    items = read_items()
    updated = False
    for item in items:
        if item.id == id:
            if name:
                item.name = name
            if price:
                item.price = price
            if quantity:
                item.quantity = quantity
            if description:
                item.description = description
            updated = True
            break
    if updated:
        save_items(items)
        print(f"Item with ID {id} updated successfully")
    else:
        print(f"Item with ID {id} not found")

def delete_item(id):
    items = read_items()
    updated_items = [item for item in items if item.id != id]
    if len(updated_items) < len(items):
        save_items(updated_items)
        print(f"Item with ID {id} deleted successfully")
    else:
        print(f"Item with ID {id} not found")

def sort_by_price():
    items = read_items()
    sorted_items = sorted(items, key=lambda x: x.price)
    for item in sorted_items:
        print(item)

# Keranjang belanja
cart = []

def add_to_cart(item_id):
    items = read_items()
    for item in items:
        if item.id == item_id:
            cart.append(item)
            print(f"{item.name} added to cart")
            return
    print(f"Item with ID {item_id} not found")

def check_out():
    total_price = sum(item.price for item in cart)
    print("Cart:")
    for item in cart:
        print(item)
    print(f"Total Price: {total_price}")
    confirm = input("Confirm order (yes/no): ")
    if confirm.lower() == 'yes':
        print("Order confirmed! Receipt:")
        for item in cart:
            print(item)
        print(f"Total Price: {total_price}")
        cart.clear()
    else:
        print("Order cancelled")

def search_item(query):
    items = read_items()
    found_items = []
    for item in items:
        if query.lower() in item.name.lower() or query == str(item.id) or query == str(item.price):
            found_items.append(item)
    if found_items:
        for item in found_items:
            print(item)
    else:
        print("No items found matching the query")

# Inisialisasi CSV jika belum ada
initialize_csv()
