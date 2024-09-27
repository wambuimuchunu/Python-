# Initialize the inventory dictionary
inventory = {}

def add_item():
    item_name = input("Enter the name of the item to add: ")
    stock_count = int(input("Enter the stock count for the item: "))
    inventory[item_name] = {"stock_count": stock_count}
    print(f"Added {item_name} with a stock count of {stock_count}.")

def update_item():
    item_name = input("Enter the name of the item to update: ")
    if item_name in inventory:
        stock_count = int(input("Enter the new stock count for the item: "))
        inventory[item_name]["stock_count"] = stock_count
        print(f"Updated {item_name} to a new stock count of {stock_count}.")
    else:
        print("Item not found in inventory.")

def remove_item():
    item_name = input("Enter the name of the item to remove: ")
    if item_name in inventory:
        del inventory[item_name]
        print(f"Removed {item_name} from inventory.")
    else:
        print("Item not found in inventory.")

def check_item_details():
    item_name = input("Enter the name of the item to check details: ")
    if item_name in inventory:
        item = inventory[item_name]
        return f"Product Name: {item_name} -> Stock Count: {item['stock_count']}"
    else:
        return "Item not found in inventory."

def display_total_quantity():
    print(inventory)
    total_quantity = sum(item["stock_count"] for item in inventory.values())
    return f"Total quantity of all items in inventory: {total_quantity} units"

def main():
    while True:
        print("\nInventory Management System")
        print("1. Add an item")
        print("2. Update an item")
        print("3. Remove an item")
        print("4. Check item details")
        print("5. Display total inventory quantity")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            print(check_item_details())
        elif choice == '5':
            print(display_total_quantity())
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
