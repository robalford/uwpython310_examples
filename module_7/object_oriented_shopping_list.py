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
                print(grocery_item.category)
            print(grocery_item.display_grocery_item())
        print(f"Total cost of groceries: {self.calculate_total_cost()}")

    def calculate_total_cost(self):
        return sum([grocery_item.price for grocery_item in self.grocery_items.values()])


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
