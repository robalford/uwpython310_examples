# In a function with positional arguments, all the arguments are required, and they must be
# provided in the order specified when the function is called

def print_args(arg1, arg2):
    print("Arg 1:", arg1)
    print("Arg 2:", arg2)


# print_args(1, 2)

# Keyword arguments allow you to include optional arguments with default values after the required positional
# arguments


def print_args(arg1, arg2, default_arg="I'm the default"):
    print("Arg 1:", arg1)
    print("Arg 2:", arg2)
    print("Default arg:", default_arg)


# But you still have to provide all the positional arguments when calling the function, or you'll get a TypeError

# print_args(1, default_arg="Override the default")

# So what if you want to accept an unknown amount of required arguments? Python provides an 'unpacking' operator '*'
# for accepting variable numbers of positional arguments using the following syntax

def print_shopping_list(*args):
    for grocery_item in args:
        print(grocery_item)


# print_shopping_list("Apples", "Peanut Butter", "Cheese")

# Using the name *args is just a convention, it's the * operator that matters so the function above could be
# rewritten like this


def print_shopping_list(*grocery_items):
    for grocery_item in grocery_items:
        print(grocery_item)


# print_shopping_list("Bread", "Canned Soup", "Yogurt")

# To accept a variable number of keyword arguments, you can use the '**' operator when defining your functions.
# You'll often see this defined as **kwargs, but like *args the name is just a convention.

# You can combine required positional arguments variable numbers of positional and keyword arguments, so there's
# lots of flexibility in writing highly dynamic functions like this

def create_user_bio(name, age, *interests, **additional_information):
    print("Name:", name)
    print("Age:", age)
    print("Interests:")
    for interest in interests:
        print("-", interest)
    for key, value in additional_information.items():
        print(f"{key.title()}: {value}")


# create_user_bio("Rob",
#                 44,
#                 "Music", "Coding", "Kayaking",
#                 occupation="Software developer",
#                 college="University of Washington")


# When the function is called, its positional arguments evaluate to a tuple and its keyword arguments
# evaluate to a dictionary. So you can also use the unpacking operators to pass in those data structures
# as variables

my_tuple = (1, 2)
my_dict = {"kwarg1": "override default1"}


def my_function(arg1, arg2, kwarg1="default1", kwarg2="default2"):
    print(arg1)
    print(arg2)
    print(kwarg1)
    print(kwarg2)


# my_function(*my_tuple, **my_dict)


# The str.format() method accepts a variable number of keyword arguments which can be passed in as
# a dictionary

madlib_dict = {
    "adjective": "funny",
    "verb ending in 'ing'": "singing",
    "plural noun": "cats",
}

madlib_text = """And be sure to look out for the 
{adjective} {verb ending in 'ing'} {plural noun}!""".format(**madlib_dict)

# print(madlib_text)

# Python provides a lot of flexibility in how you call your functions using required and optional arguments

# You can use all positional arguments - but they must be provided in order

# my_function(1, 2, "override default1", "override default2")

# Or you can use all keyword args and provide the args in any order

# my_function(arg2=2, kwarg1="override default1", arg1=1, kwarg2="override default2")

# You can omit the keyword arguments to use their default values

# my_function(arg2=2, arg1=1, kwarg2="override default2")

# But you are always required to provide all positional requirements

# my_function(kwarg1="override default1", arg1=1, kwarg2="override default2")

# You can also define keyword only arguments by separating positional arguments and keyword only arguments
# with an *


def keyword_only_args(arg1, arg2, *, kwarg1="default1", kwarg2="default2"):
    print(arg1)
    print(arg2)
    print(kwarg1)
    print(kwarg2)


# Now this won't work

# keyword_only_args(1, 2, "override default1", "override default2")

# But this will - and will use the default if not provided

keyword_only_args(1, 2, kwarg1="override default1")
