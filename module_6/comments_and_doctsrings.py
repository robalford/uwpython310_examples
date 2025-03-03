import math

# When to use inline comments

# Don't use for code that is self-explanatory and try to write self-documenting code with good
# naming practices


def yell(words):
    print(f"{words.upper()}!")


# Yell some words - UNNECESSARY COMMENT
yell("some word")

# Use inline comments to provide additional context or explanation for your code - for other
# devs or your future self

# Excerpt of example take_donation() function from mailroom with helpful commenting to explain logic
# and reasoning behind implementation choices


def take_donation():
    """
    Ask user for donation amount, and then add it  to the DB
    """
    # Now prompt the user for a donation amount to apply. Since this is
    # also an exit point to the main menu, we want to make sure this is
    # done before mutating the db.
    name = input("Enter a donor name (new or existing): \n >")
    while True:
        amount_str = input("Enter a donation amount (or <enter> to exit)> ").strip()
        if not amount_str:
            # if they provide no input, go back to previous menu
            return
        # Make sure amount is a valid amount before leaving the input loop
        try:
            amount = float(amount_str)
            # extra check here -- unlikely that someone will type "NaN", but
            # it IS possible, and it is a valid floating point number:
            # http://en.wikipedia.org/wiki/NaN
            if math.isnan(amount) or math.isinf(amount) or round(amount, 2) == 0.00:
                raise ValueError
        except ValueError:
            print("error: donation amount is invalid\n")
            continue
        else:
            break


# Can use comments to record places in the code you want to revisit, refine or refactor

# TODO: make this function actually do something
def place_holder():
    pass


# Docstrings

# If a string literal is the first thing in the function Python interprets it as a docstring
# that can be accessed with the function's __doc__ attribute.

# Docstrings can be formatted to automatically generate written documentation for your functions
# using a tool called Sphinx and a markup language called reStructured Text as shown below.

# They also provide a nice format for clearly documenting your functions and the parameters they accept directly in
# your code - there are different styles of docstring formatting including javadoc and Google style - most Python
# devs use reStructured Text style because it works with Sphinx and other formatting / documentation tools.

def my_function(param1, param2):
    """
    Describe what the function does in a single line.

    If needed you can add some additional lines of documentation
    after the single summary line. Always use triple quotes, even
    for a single line to follow convention and allow you to expand
    the documentation to multiple lines at a later time.

    :param param1: this is a first param
    :param param2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    pass


print(my_function.__doc__)
