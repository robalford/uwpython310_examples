from textwrap import dedent


def get_shopping_list():
    return {
        'produce': [
            {'item': 'apples', 'checked_off': True},
            {'item': 'bananas', 'checked_off': False},
            {'item': 'lettuce', 'checked_off': False},
        ],
        'dairy': [
            {'item': 'milk', 'checked_off': False},
            {'item': 'butter', 'checked_off': True},
        ],
        'meat/poultry': [
            {'item': 'chicken', 'checked_off': False},
            {'item': 'hamburger', 'checked_off': False},
        ],
    }


def print_shopping_list():
    for category, items in shopping_list.items():
        print(f"{category.title()}:\n")
        for item in items:
            print(f"[{'x' if item['checked_off'] else ' '}] {item['item'].title()}")
        print("\n")


def display_welcome_message():
    print(dedent("""
    Welcome to MyShoppingList!

    Choose from the following options:
    1: Print shopping list
    2: Update shopping list
    3: Stop shopping
    """))


def display_update_message():
    print(dedent("""
    Update options:

    1: Add item to shopping list
    2: Check off item
    3: Remove item
    """))


def add_item():
    category = input("Enter shopping item category: \n>>> ").strip().lower()
    if category not in shopping_list:
        print("Invalid category")
    else:
        item_to_add = input("Enter item to add to list: \n>>> ").strip().lower()
        shopping_list[category].append({'item': item_to_add, 'checked_off': False})
        print(f"{item_to_add} added to shopping list")


def check_off_item():
    item_to_check_off = input("Enter item to check off: \n>>> ").strip().lower()
    checked_off_item = False
    for items in shopping_list.values():
        for item in items:
            if item['item'] == item_to_check_off:
                item['checked_off'] = True
                print(f"Checked off: {item_to_check_off.title()}")
                checked_off_item = True
    if not checked_off_item:
        print("That item is not in your shopping list.")


def remove_item():
    item_to_remove = input("Enter item to remove from list: \n>>> ").strip().lower()
    removed_item = False
    for category_items in shopping_list.values():
        for item in category_items[:]:
            if item_to_remove == item['item']:
                category_items.remove(item)
                print(f"Removed {item_to_remove} from shopping list.")
                removed_item = True
    if not removed_item:
        print("That item is not in your shopping list.")


def update_shopping_list():
    display_update_message()
    update_options = {
        "1": add_item,
        "2": check_off_item,
        "3": remove_item,
    }
    update_selection = input(">>> ")
    update_option = update_options.get(update_selection)
    if update_option is None:
        print("Invalid selection")
    else:
        update_option()


def main():
    program_running = True
    while program_running:
        display_welcome_message()
        home_screen_selection = input(">>> ")
        # Dict as switch is an alternative syntax to match/case and chained if statements
        if home_screen_selection == '1':
            print_shopping_list()
        elif home_screen_selection == '2':
            update_shopping_list()
        elif home_screen_selection == '3':
            program_running = False
        else:
            print("Invalid selection.")


if __name__ == "__main__":
    shopping_list = get_shopping_list()
    main()
