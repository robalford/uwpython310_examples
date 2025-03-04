# Comprehensions are a unique Python language feature that provide a concise syntax for performing
# operations on all items in a sequence in order to create a new sequence

# These are similar to concepts like map() and filter() functions in functional programming languages
# (and Python provides built-in map() and filter() functions as well that pre-date comprehensions)

# Python is an object-oriented programming language that supports some functional programming language
# features to use where they make sense (like a lot of things in Python)

# A comprehension is used apply an expression to each member of a sequence in order to create another
# sequence

# So to do something like this:

lower_case_list = ["comprehensions", "are", "cool"]

upper_case_list = []

for lower_case_word in lower_case_list:
    upper_case_list.append(lower_case_word.upper())

# print(upper_case_list)

# You can use a list comprehension like this:

upper_case_list = [lower_case_word.upper() for lower_case_word in lower_case_list]

# print(upper_case_list)

# You can use any Python expression inside a comprehension along with a for loop statement to generate a
# new list of items generated from the expression. You get the same result with a less code which is nicely
# Pythonic

# Comprehensions also work with nested loops. So the follow code:

list1 = [1, 2, 3]
list2 = [3, 2, 1]

multiplied_lists = []

for number1 in list1:
    for number2 in list2:
        multiplied_lists.append(number1 * number2)


# print(multiplied_lists)


# Can be written as a list comprehension like this:

multiplied_lists = [number1 * number2 for number1 in list1 for number2 in list2]

# print(multiplied_lists)


# In functional programming a map() function applies the same function to every member in a sequence and
# creates a new iterable object

def multiply_by_two(number):
    return number * 2


multiplied_by_two = []

for n in map(multiply_by_two, list1):
    multiplied_by_two.append(n)

# print(multiplied_by_two)

# In a list comprehension, this can be simplified to this:

multiplied_by_two = [number * 2 for number in list1]

# print(multiplied_by_two)


# Python also provides a filter() function that creates a new sequence with only certain elements from the
# original sequence. It is basically a shorthand function for implementing the following filtering logic:

one_through_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
one_through_five = []

for number in one_through_ten:
    if number <= 5:
        one_through_five.append(number)

# print(one_through_five)

# But with a comprehension, you can include mapping and filtering in a single concise statement

one_through_five_times_five = [number * 5 for number in one_through_ten if number <= 5]

# print(one_through_five_times_five)

# Python supports set and dictionary comprehensions like the following as well:

five_times_table = {number: number * 5 for number in one_through_ten}

# print(five_times_table)
