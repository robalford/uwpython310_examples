# Use clear, specific names for variables, functions and classes in your programs

# Don't do this

stuff = ["Apple", "Cereal", "Paper Towels"]

for thing in stuff:
    print(thing)

# This is better

shopping_list = ["Apple", "Cereal", "Paper Towels"]

for item in shopping_list:
    print(item)

# But 'item' is still pretty vague - so this is even better

for grocery_item in shopping_list:
    print(grocery_item)

# Only use single letter names for conventions like indexes, or unused variables in a single scope

for i, grocery_item in enumerate(shopping_list):
    print(i, grocery_item)

for _ in range(10):
    print("*")

# Reuse the same name when modifying a variable

grocery_item = "apple"
grocery_item = grocery_item.title()

# Don't use 'Hungarian Notation' in Python because of dynamic typing

int_age = 43
print("Age: " + str(int_age))  # int_age is now a string


# Function names should clearly describe the action they perform - helps to focus on functions that do just one thing

def add_grocery_item(new_grocery_item):
    shopping_list.append(new_grocery_item)
