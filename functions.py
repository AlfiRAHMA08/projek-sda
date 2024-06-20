import csv
from os import system, name

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


def addItem(name, price, quantity, description):
    new_id = createId()
    if new_id is None:
        return  # if there was an error creating the ID

    with open('data.csv', 'a', newline='') as file:
        fieldnames = ['id', 'name', 'price', 'quantity', 'description']
        
        # Check if the file is empty
        file_empty = file.tell() == 0
        csv_appender = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)
        
        # write only if the file is empty
        if file_empty:
            csv_appender.writeheader()
        
        csv_appender.writerow({'id': new_id, 'name': name, 'price': price, 'quantity': quantity, 'description': description})
        print(f"Item successfully added!")


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
            print(f"Item with ID '{item_id}' not found.")
        else:
            print(f"Item with ID '{item_id}' has been updated.")
    except FileNotFoundError:
        print("The file 'data.csv' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def searchItem(identity):
    try:
        with open('data.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            for line in csv_reader:
                if line['id'] == identity:
                    print(f"Name: {line['name']}\nPrice: {line['price']}\nStock: {line['quantity']}\nDescription: {line['description']}")
                    return line
            print(f"Item with the id '{identity}' not found.")
    except FileNotFoundError:
        print("The file 'data.csv' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


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
            print(f"Item with ID '{item_id}' not found.")
        else:
            print(f"Item with ID '{item_id}' has been deleted.")
    except FileNotFoundError:
        print("The file 'data.csv' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def enterToContinue():
    input("Press enter to continue")
    clear()


if __name__ == "__main__":
    print(f"Hi mom")
