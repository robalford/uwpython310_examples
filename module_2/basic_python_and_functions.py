#!/usr/bin/env python

# The simplest Python program

print("Hello world!")

# Values and data

integer_type = 7
float_type = 2.5
string_type = "I am a string"
boolean_type = True
none_type = None

# Lines of code

# Commented out print statement

# I'm a comment

# print("Stop ignoring me!")

# Variable assignment statement that contains an expression

statement = 2  # statement
print(2 +2)  # printed expression

statement_contains_expression = 2 + 2

# Blocks of code - COPY THIS

learning_python = True

if learning_python:
    print("Code blocks are defined by colon and indentation.")
    print("Remember white space is significant!")
    print("Use spaces not tabs please :)")

# Expressions - COPY THESE

calculate_me = 120 / 4 * 3 + 2
print(calculate_me)

floor_me = 120 // 4 * 3 + 2
print(floor_me)

add_me = 2 + 2
concatenate_me = '2' + '2'
print(add_me)
print(concatenate_me)

# confuse_me = 2 + '2'
# print(confuse_me)

convert_me = 2 + int('2')
print(convert_me)

# Symbols / variables

_symbol = 23
symbol = 23
# 23symbol = 23

# Naming conventions

snake_case = "Use me for variable and function names"


class UseCamelCaseForClasses:
    CONSTANT_VALUE = "Use ALL_CAPS for constants"

# Assignment (next slide) - symbols don't have types, values do - dynamic typing

symbol = 23
print(type(symbol))

symbol = "23"
print(type(symbol))

# In place assignment

symbol = 23
symbol += 23
print(symbol)

# Multiple values and value swapping

value_1, value_2 = 1, 2
print(value_1)
print(value_2)

value_1, value_2 = value_2, value_1
print(value_1)
print(value_2)

# Value identity - NEXT SLIDE

symbol_1 = 1
symbol_2 = 2
print(id(symbol_1))
print(id(symbol_2))
print(symbol_1 is symbol_2)

symbol_2 = symbol_1
print(symbol_1 is symbol_2)

# Value equality

symbol_1 = 1
symbol_2 = "1"
print(symbol_1 == symbol_2)

# Deleting

symbol = 1
del symbol
# print(symbol)

# Exceptions

# print(unbound_symbol)  # NameError
# bad_math = 2 + '2'  # TypeError
# class = 'Python 310'  # SyntaxError
# symbol = "string"
# print(symbol.title())
# symbol = 5
# print(symbol.title())  # AttributeError

# String literals

print("I'm a string")
print('I\'m also a string')
print("""I'm a 
a multi-line
string""")
print(r'I\'m a raw string')

# Lists, for loops and conditionals

shopping_list = ["oatmeal", "candy", 2, True]

for item in shopping_list:
    print(item)

for number in range(10):
    print(number)

# change these values to show different paths

i_am_hungry = True
i_am_thirsty = False

if i_am_hungry:
    print("Eat something")
elif i_am_thirsty:
    print("Drink something")
else:
    print("Keep doing what you're doing")

# Assert statement - writing tests

def add(num1, num2):
    return num1 + num2

assert add(2, 2) == 4
# assert add(2, 2) == 22

# Functions, defining function, calling functions

# do_nothing()  # called before defined error

def do_nothing():
    pass

def do_something():
    print("I'm doing it!")

def return_something():
    return 2 + 2

print(do_nothing())
print(return_something())

def return_once():
    return 2 + 2
    print("I'm doing it!")

print(return_once())

def multiple_return_values():
    return 2, 4

symbol_1, symbol_2 = multiple_return_values()

print(symbol_1)
print(symbol_2)

def function_in_function():
    do_something()
    return 2 + 2

print(function_in_function())

# Viewing the call stack

def divide_by_zero():
    5 / 0

def call_divide_by_zero():
    divide_by_zero()

def view_call_stack():
    call_divide_by_zero()

# view_call_stack()

# Function parameters and arguments

def function_with_parameters(param_1, param_2):
    print(param_1, param_2)

function_with_parameters('hello ', 'world!')

def function_with_optional_parameters(param_1="hello ", param_2="world!"):
    print(param_1, param_2)

function_with_optional_parameters()
function_with_optional_parameters(param_2="python!")

def function_with_required_and_optional_parameters(im_required, so_am_i, im_optional="I'm optional"):
    print(im_required, so_am_i, im_optional)

function_with_required_and_optional_parameters("I'm required", "So am I")
function_with_required_and_optional_parameters("I'm required", "So am I",
                                               im_optional="But nice to have!")
# function_with_optional_parameters(im_optional="This will not work", "I'm required", "So am I")
