import csv
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

# Fungsi untuk membuat ID baru
def createId():
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            last_id = 0
            for row in csv_reader:
                last_id = int(row['id'])
            return last_id + 1
    except FileNotFoundError:
        return 1
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Fungsi untuk menambahkan item
def addItem(name, price, quantity, description):
    new_id = createId()
    if new_id is None:
        return  # jika terjadi kesalahan saat membuat ID

    with open('data.csv', 'a', newline='') as file:
        fieldnames = ['id', 'name', 'price', 'quantity', 'description']
        
        # Cek apakah file kosong
        file_empty = file.tell() == 0
        csv_appender = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        
        # Menulis header hanya jika file kosong
        if file_empty:
            csv_appender.writeheader()
        
        csv_appender.writerow({'id': new_id, 'name': name, 'price': price, 'quantity': quantity, 'description': description})
        messagebox.showinfo("Info", "Item successfully added!")

# Fungsi untuk memperbarui item
def updateItem(item_id, name=None, price=None, quantity=None, description=None):
    updated = False
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)

        with open('data.csv', 'w', newline='') as file:
            fieldnames = ['id', 'name', 'price', 'quantity', 'description']
            csv_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in rows:
                if int(row['id']) == item_id:
                    if name:
                        row['name'] = name
                    if price:
                        row['price'] = price
                    if quantity:
                        row['quantity'] = quantity
                    if description:
                        row['description'] = description
                    updated = True
                csv_writer.writerow(row)

        if not updated:
            messagebox.showwarning("Warning", f"Item with ID '{item_id}' not found.")
        else:
            messagebox.showinfo("Info", f"Item with ID '{item_id}' has been updated.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'data.csv' does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Fungsi untuk mencari item
def searchItem(identity):
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                if line['id'] == identity:
                    result = f"Name: {line['name']}\nPrice: {line['price']}\nStock: {line['quantity']}\nDescription: {line['description']}"
                    messagebox.showinfo("Info", result)
                    return line
            messagebox.showwarning("Warning", f"Item with the id '{identity}' not found.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'data.csv' does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Fungsi untuk menghapus item
def deleteItem(item_id):
    deleted = False
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            rows = list(csv_reader)

        with open('data.csv', 'w', newline='') as file:
            fieldnames = ['id', 'name', 'price', 'quantity', 'description']
            csv_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in rows:
                if int(row['id']) != item_id:
                    csv_writer.writerow(row)
                else:
                    deleted = True

        if not deleted:
            messagebox.showwarning("Warning", f"Item with ID '{item_id}' not found.")
        else:
            messagebox.showinfo("Info", f"Item with ID '{item_id}' has been deleted.")
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'data.csv' does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Fungsi untuk menghapus semua item
def clear():
    with open('data.csv', 'w', newline='') as file:
        fieldnames = ['id', 'name', 'price', 'quantity', 'description']
        csv_writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        csv_writer.writeheader()
    messagebox.showinfo("Info", "All items have been cleared.")

# Fungsi untuk menampilkan semua item
def showAllItems():
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            all_items = list(csv_reader)
            
            if not all_items:
                messagebox.showinfo("Info", "No items found.")
                return
            
            display_text = ""
            for item in all_items:
                display_text += f"ID: {item['id']}\nName: {item['name']}\nPrice: {item['price']}\nStock: {item['quantity']}\nDescription: {item['description']}\n\n"
            
            showItemsWindow = tk.Toplevel(root)
            showItemsWindow.title("All Items")
            text_area = scrolledtext.ScrolledText(showItemsWindow, wrap=tk.WORD, width=50, height=20)
            text_area.pack(pady=10, padx=10)
            text_area.insert(tk.END, display_text)
            text_area.config(state=tk.DISABLED)
    except FileNotFoundError:
        messagebox.showerror("Error", "The file 'data.csv' does not exist.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
