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

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.product_id},{self.name},{self.price},{self.quantity}"

class ECommercePlatform:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def read_products(self):
        for product in self.products:
            print(product)

    def update_product(self, product_id, name=None, price=None, quantity=None):
        for product in self.products:
            if product.product_id == product_id:
                if name:
                    product.name = name
                if price:
                    product.price = price
                if quantity:
                    product.quantity = quantity
                return True
        return False

    def delete_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return True
        return False

    def sort_products(self):
        self.products.sort(key=lambda x: x.name)

    def search_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def import_csv(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  
            for row in reader:
                product_id, name, price, quantity = row
                product = Product(product_id, name, float(price), int(quantity))
                self.add_product(product)

def main():
    platform = ECommercePlatform()

    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Sort Products")
        print("6. Search Product")
        print("7. Import Products from CSV")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            product = Product(product_id, name, price, quantity)
            platform.add_product(product)
            print("Product added successfully.")
        
        elif choice == '2':
            platform.read_products()
        
        elif choice == '3:

if __name__ == "__main__":
    main()
  
print(f"Hi mom")
