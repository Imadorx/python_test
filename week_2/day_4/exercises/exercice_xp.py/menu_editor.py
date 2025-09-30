from menu_item import MenuItem
from menu_manager import MenuManager

def show_user_menu():
    while True:
        print("\nMenu Editor Options:")
        print("V - View an Item")
        print("A - Add an Item")
        print("D - Delete an Item")
        print("U - Update an Item")
        print("S - Show Restaurant Menu")
        print("E - Exit")

        choice = input("Choose an option: ").upper()

        if choice == "V":
            name = input("Enter item name: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"Found: {item['name']} - {item['price']}")
            else:
                print("Item not found.")

        elif choice == "A":
            add_item_to_menu()

        elif choice == "D":
            remove_item_from_menu()

        elif choice == "U":
            update_item_from_menu()

        elif choice == "S":
            show_restaurant_menu()

        elif choice == "E":
            print("\n Exiting... Final Restaurant Menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid choice, try again.")

def add_item_to_menu():
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    item = MenuItem(name, price)
    item.save()

def remove_item_from_menu():
    name = input("Enter item name to delete: ")
    item = MenuItem(name, 0)
    item.delete()

def update_item_from_menu():
    old_name = input("Enter current item name: ")
    new_name = input("Enter new name: ")
    new_price = int(input("Enter new price: "))
    item = MenuItem(old_name, 0)
    item.update(new_name, new_price)

def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("\n Restaurant Menu:")
        for i in items:
            print(f"- {i['name']} : {i['price']} MAD")
    else:
        print("The menu is empty.")

if __name__ == "__main__":
    show_user_menu()
