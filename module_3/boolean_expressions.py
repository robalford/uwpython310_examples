# Boolean expressions

boolean_variable = True

# Testing for truthiness

make_me_a_boolean = 0

bool(make_me_a_boolean)  # returns False

# Pythonic booleans and conditional statements

if boolean_variable == True:
    print("This is not Pythonic")

if boolean_variable:
    print("Much better")

sunny = True
mood = ""

mood = "Good" if sunny else "Bad"

print(mood)

# Boolean operators

print(not True)

print(0 and 1)  # and returns the first operand that is False

print(0 or 1)  # or returns the first operand that is True

print(0 and 10/0)  # be careful, this can hide bugs

print(1 and 2 and 0 and 3)  # chaining boolean operators

# Pythonic conditionals with and, or and not

sunny = True
the_weekend = False

if sunny and the_weekend:
    print("Go to the beach!")

if sunny or the_weekend:
    print("Take a walk outside")

if not the_weekend:
    print("Go to work")


