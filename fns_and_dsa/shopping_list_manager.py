# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # array to hold items
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"Added: {item}")
            else:
                print("No item entered. Nothing added.")
        elif choice == '2':
            item = input("Enter item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed: {item}")
            else:
                print(f"Item '{item}' not found in your shopping list.")
        elif choice == '3':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your shopping list:")
                for idx, it in enumerate(shopping_list, start=1):
                    print(f"{idx}. {it}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
