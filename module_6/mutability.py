import copy

# Mutable objects can have their contents changed in place, immutable objects cannot

mutable_list = [1, 2, 3]
mutable_list[1] = 0
# print(mutable_list)

immutable_tuple = (1, 2, 3)
# immutable_tuple[1] = 0

# This causes a couple 'gotcha' conditions in Python that can be super tricky to debug if you aren't
# aware of them

# One of these conditions is using mutable objects inside a container

# Consider this list object which contains multiple lists

list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
]

# If we make a copy of this list, we get an entirely new object

list_of_lists_copy = list_of_lists[:]

# print(list_of_lists_copy is list_of_lists)

# However, if we mutate one of the elements inside the copy

list_of_lists_copy[1].append(7)

# The object in the original list gets mutated as well

# print(list_of_lists)

# That's because they are the same object

# print(list_of_lists_copy[1] is list_of_lists[1])

# When Python makes a copy of a container, it makes a 'shallow copy' by default. That means it creates
# a new container object that includes references to all the same objects as the original container. Usually
# this is fine and takes the least amount of work. But can lead to bugs when the containers contain mutable
# objects.

# If you need to make a new copy of all the objects in the container, you can use the copy.deepcopy() function
# from the Python Standard Library

list_of_lists_deepcopy = copy.deepcopy(list_of_lists)

list_of_lists_deepcopy[1].append(8)
# print(list_of_lists_deepcopy)
# print(list_of_lists)

# Another mutability 'gotcha' happens when using mutable objects as default function arguments

# Suppose you want to accept a list as a function parameter, and then add some items to the list inside the
# function. It would make sense to use an empty list as a default function parameter if another list is not
# provided as an argument to the function call. Something like this:


def add_numbers_to_list(list_of_nums=[]):
    for number in range(10):
        list_of_nums.append(number)
    return list_of_nums


# But then, every time you call the function with the default list value, it adds more items to the original
# list

# print(add_numbers_to_list())
# print(add_numbers_to_list())
# print(add_numbers_to_list())

# That's because the default argument is defined when the function is created - and every time it's called
# it will refer back to the same list object that was assigned in the function definition

# To avoid this situation and accept an empty list as a default function argument, you can use this
# common work-around:


def add_numbers_to_list(list_of_nums=None):
    if list_of_nums is None:
        list_of_nums = []
    for number in range(10):
        list_of_nums.append(number)
    return list_of_nums


# Now you get the expected behavior where the function uses a new empty list each time it's called

print(add_numbers_to_list())
print(add_numbers_to_list())
