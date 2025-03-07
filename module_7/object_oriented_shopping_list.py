from textwrap import dedent
import sys


class GroceryItem:
    def __init__(self, name, category, price=None):
        self.name = name
        self.category = category
        self.price = price
        self.checked_off = False

    def display_grocery_item(self):
        return (f"[{'x' if self.checked_off else ' '}] "
                f"{self.name.title()} {self.price:.2f}")


class ShoppingList:
    def __init__(self, name):
        self.name = name
        self.grocery_items = {}

    def add_grocery_item(self, grocery_item):
        self.grocery_items[grocery_item.name] = grocery_item

    def print_shopping_list(self):
        items_sorted_by_category = sorted(self.grocery_items.values(), key=lambda item: item.category)
        current_category = items_sorted_by_category[0].category
        print(current_category.title())
        for grocery_item in items_sorted_by_category:
            if grocery_item.category != current_category:
                current_category = grocery_item.category
                print(grocery_item.category.title())
            print(grocery_item.display_grocery_item())
        print(f"Total cost of groceries: {self.calculate_total_cost()}")

    def calculate_total_cost(self):
        return sum([grocery_item.price for grocery_item in self.grocery_items.values()])


# Create a shopping list

milk = GroceryItem("milk", "dairy", 5.00)
lettuce = GroceryItem("lettuce", "produce", 2.00)
chicken = GroceryItem("chicken", "meat", 10.00)
cheese = GroceryItem("cheese", "dairy", 7.00)
hotdogs = GroceryItem("hot dogs", "meat", 6.00)
apples = GroceryItem("apples", "produce", 4.00)
yogurt = GroceryItem("yogurt", "dairy", 6.00)


shopping_list = ShoppingList("QFC")
shopping_list.add_grocery_item(milk)
shopping_list.add_grocery_item(lettuce)
shopping_list.add_grocery_item(chicken)
shopping_list.add_grocery_item(cheese)
shopping_list.add_grocery_item(hotdogs)
shopping_list.add_grocery_item(apples)
shopping_list.add_grocery_item(yogurt)

shopping_list.print_shopping_list()


# User Interaction Code - these work best as module-level functions

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
    item_to_add = input("Enter item to add to list: \n>>> ").strip().lower()
    while not item_to_add:
        item_to_add = input("You must enter an item to continue: \n>>> ").strip().lower()
    category = input("Enter shopping item category: \n>>> ").strip().lower() or "Other"
    while True:
        try:
            price = float(input("Enter shopping item price: \n>>> ").strip().lower())
        except ValueError:
            print("Price must be a number.")
        else:
            break
    new_grocery_item = GroceryItem(item_to_add, category, price)
    shopping_list.add_grocery_item(new_grocery_item)
    print(f"Added {item_to_add} to shopping list.")


def check_off_item():
    item_to_check_off = input("Enter item to check off: \n>>> ").strip().lower()
    if item_to_check_off not in shopping_list.grocery_items:
        print("That item is not in your shopping list.")
    else:
        shopping_list.grocery_items[item_to_check_off].checked_off = True
        print(f"Checked off {item_to_check_off}.")


def remove_item():
    item_to_remove = input("Enter item to remove from list: \n>>> ").strip().lower()
    if item_to_remove not in shopping_list.grocery_items:
        print("That item is not in your shopping list.")
    else:
        del shopping_list.grocery_items[item_to_remove]
        print(f"Removed {item_to_remove} from shopping list.")


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
    main_menu_options = {
        "1": shopping_list.print_shopping_list,
        "2": update_shopping_list,
        "3": sys.exit,
    }
    while True:
        display_welcome_message()
        home_screen_selection = input(">>> ")
        menu_option = main_menu_options.get(home_screen_selection)
        if menu_option is None:
            print("Invalid selection.")
        else:
            menu_option()


if __name__ == "__main__":
    main()
