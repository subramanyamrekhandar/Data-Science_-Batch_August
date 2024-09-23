#  Problem: To adding Numpy Functionality to calculate total inventory values 
#  Solution: We will use numpy library to calculate total inventory values

import json
import numpy as np


# 1. add ( create)
# 2. view 
# 3. delete 
# 4. update


def create_item(idno, item, quantity, price):

    data = {
        "idno": idno,
        "item": item,
        "qunatity": quantity,
        "price": price 
    }
   
    with open("numpy.json", "w") as file:
        json.dump(data, file, indent=4)

def view_item():
    with open('numpy.json', "r") as file:
        data = json.load(file)
    print(data)
        
            
def update_item(idno, item):

    try: 
        with open('numpy.json', "r") as file:
            data = json.load(file)
    except FileExistsError:
        print("File does not exist")
        return 

   
    if data["idno"] == idno:   # 1= 1  
        data["item"] = item

   
     

    with open("numpy.json", "w") as file:
        json.dump(data, file, indent=4)


def delete_item(idno):
    try: 
        with open('numpy.json', "r") as file:
            data = json.load(file)
    except FileExistsError:
        print("File does not exist")
        return 
    

    if data["idno"] == idno:
        data = {}
    
    with open("numpy.json", "w") as file:
        json.dump(data, file, indent=4)
    
def calculate_total_value():
    try: 
        with open("numpy.json", "r") as file:
            data = json.load(file)

            quantities = np.array([data["qunatity"]])
            prices = np.array([data["price"]])
            total_value = np.sum(quantities * prices)
            print(f"Total Values: ${total_value:.2f}")
            
    except FileNotFoundError:
        print("File is empty")

# Menu System 

def main():
    while True:
        print("\n This is Inventory Management System here")
        print("1. Create Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. cal total value")
        print("6. exit")


        # menu input value system
        choice = input("Enter the Your Menu:")

        # Menu system here
        if choice == "1":
            idno = input("Enter the idno: ")
            item = input("Enter the item: ")
            quantity = int(input("Enter the Quantity: "))
            price = float(input("Enter the Price: "))
            create_item(idno, item, quantity, price)
        elif choice == "2":
            view_item()
        elif choice == "3":
            idno = input("Enter the idno: ")
            item = input("Enter the item: ")
            # quantity = int(input("Enter the Quantity: "))
            update_item(idno, item)
        elif choice == "4":
            idno = input("Enter the idno: ")
            delete_item(idno)
        elif choice == "5":
            calculate_total_value()
        elif choice == "6":
            print("Thanks for using this Inventory Management System")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# calling function
# if __name__ == "__main__":
main()       
