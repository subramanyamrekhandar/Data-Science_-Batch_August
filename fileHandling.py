# to manage and store data by using inventory management syatem
# Methods
# write, read, update, delete
# Modes
# read, write, append, 

# like Implementing the MENU System here 

# create the data
def create_item(idno, item, quantity, price):
    with open("inventory.txt", "a") as file:
        file.write(f"{idno}, {item}, {quantity}, {price}\n")

# View the data ( read)
def view_item():
    with open("inventory.txt", "r") as file:
        for line in file:
            print(line)

# Update the Data
def update_item(idno, item):
    lines = []
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
    
    with open("inventory.txt", "w") as file:
        for line in lines:
            if line.startswith(idno):
                X = line.strip().split(",")
                file.write(f"{X[0]}, {item}\n")
            else:
                file.write(line)
    
# delete data
def delete_item(idno):
    lines = []
    with open("inventory.txt", "r") as file:
        lines = file.readlines()
    with open("inventory.txt", "w") as file:
        for line in lines:
            if not line.startswith(idno):
                file.write(line)

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
            item = input("Enter the item: ")
            quantity = int(input("Enter the Quantity: "))
            price = float(input("Enter the Price: "))
            create_item(idno, item, quantity, price)
        elif choice == "2":
            view_item()
        elif choice == "3":
            idno = input("Enter the idno: ")
            item = input("Enter the item: ")
            update_item(idno, item)
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

