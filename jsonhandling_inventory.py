import json 

# data = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# # METHODS
# write = dump
# read = load

# # MODES
# r = r
# w = w



# with open("jasondata.json", "w") as json_file:
#     json.dump(data, json_file)

# with open("jasondata.json", "r") as json_file:
#     X = json.load(json_file)
# print(X)
   
def create_item(idno, itemName, quantity, price):

    content = {
        # KEY = Values
        "idno": idno,
        "itemName": itemName,
        "quantity": quantity,
        "price": price
    }
    with open("jasondata.json", "w") as file:
        json.dump(content, file, indent=4)

def view_item():
    with open("jasondata.json", "r") as file:
        X = json.load(file)
    print(X)

def update_item(idno, itemName, quantity):
    try:
        with open("jasondata.json", "r") as file:
            content = json.load(file)

    except FileExistsError:
        print("data is empty")
        return
    
    if content["idno"] == idno:
        content["itemName"] = itemName,
        content["quantity"] = quantity
    

    with open("jasondata.json", "w") as file:
        json.dump(content, file, indent=3)

def delete_item(idno):
    try:
        with open("jasondata.json", "r") as file:
            content = json.load(file)
    except FileExistsError:
        print("didn't match here!")
        return
    
    if content["idno"] == idno:
        content={}
    
    with open("jasondata.json", "w") as file:
        json.dump(content, file, indent=4)

# Menu System 
def main():
    while True:
        print("\n This is Inventory Management System here")
        print("1. Create Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")


        # menu input value system
        choice = input("Enter the Your Menu:")

        # Menu system here
        if choice == "1":
            idno = input("Enter the idno: ")
            itemName = input("Enter the item: ")
            quantity = int(input("Enter the Quantity: "))
            price = float(input("Enter the Price: "))
            create_item(idno, itemName, quantity, price)
        elif choice == "2":
            view_item()
        elif choice == "3":
            idno = input("Enter the idno: ")
            itemName = input("Enter the item: ")
            quantity = int(input("Enter the Quantity: "))
            update_item(idno, itemName, quantity)
        elif choice == "4":
            idno = input("Enter the idno: ")
            delete_item(idno)
        elif choice == "5":
            print("Thanks for using this Inventory Management System")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# calling function
# if __name__ == "__main__":
main()       


