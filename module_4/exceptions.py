import random

# Exception Handling

def try_except_example():
    try:
        an_error = 1 / 0
    except ZeroDivisionError:
        print("You can't divide by zero!")

try_except_example()

def try_except_with_else():
    try:
        print("I'm trying!")
        if random.choice([1, 2, 3]) == 3:
            an_error = 1 / 0
    except ZeroDivisionError:
        print("I failed :(")
    else:
        # This block only run if no exceptions were raised
        print("And I succeeded!")

try_except_with_else()

def try_except_with_finally():
    try:
        print("I'm trying!")
        if random.choice([1, 2, 3]) == 3:
            an_error = 1 / 0
    except ZeroDivisionError:
        print("I failed :(")
    finally:
        # This block will always run
        print("Either way I gave it my best.")

try_except_with_finally()

# Python Exception Objects

# Check out all the Exception objects Python provides:

python_exception_objects = [name for name in dir(__builtins__) if "Error" in name]

for obj in python_exception_objects:
    print(obj)

# Don't do this (bare except statements allow unforeseen errors to pass silently)

def no_bare_except():
    try:
        bad_idea = 1 / 0
        another_bad_idea = random.not_an_attribute
        yet_another = "2" + 2
    except:
        print("Let's just pretend that didn't happen..")

no_bare_except()

# Using Exception Objects

def using_exception_objects():
    try:
        bad_math = "2" + 2
    except TypeError as error:
        print(f"Look at all this stuff we can use: {dir(error)}")
        print(f"Error: {error.args[0]}")

using_exception_objects()

def handling_multiple_exceptions():
    # Handle multiple exceptions in the same way by listing in single except statement
    try:
        bad_idea = 1 / 0
        another_bad_idea = random.not_an_attribute
        yet_another = "2" + 2
    except (ZeroDivisionError, AttributeError, TypeError) as error:
        print("Caught all expected errors")

    # Handle each exception separately with multiple except statements. The first exception encountered in the
    # try block will be handled each time (test by commenting out lines in try block)
    try:
        bad_idea = 1 / 0
        another_bad_idea = random.not_an_attribute
        yet_another = "2" + 2
    except ZeroDivisionError:
        print("You can't divide by zero!")
    except AttributeError:
        print("There's no such attribute!")
    except TypeError:
        print("You can't concatenate a string and a number!")

handling_multiple_exceptions()

# Raising Exceptions

def raise_an_exception(number):
    if type(number) not in [int, float]:
        raise TypeError(f"{number} is not a numeric type")
    double_the_number = number + number
    return double_the_number

def errors_move_up_the_call_stack():
    double_num = raise_an_exception("2")

# errors_move_up_the_call_stack()  # uncomment to throw an uncaught exception - see custom message in traceback

def handle_error():
    try:
        double_num = raise_an_exception("2")
    except TypeError as error:
        print(f"Error: {error.args[0]}")

handle_error()
