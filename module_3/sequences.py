# Sequences

a_string = "I am a string of characters"
a_list = ["I", "am", "a", "list", "of", "strings"]

# Indexing

print(a_string[0])
print(a_list[0])

print(a_string[5])
print(a_list[5])

print(a_string[-1])
print(a_list[-1])

# print(a_list[20])  # will raise IndexError

# Slicing

string_slice = a_string[5:13]
list_slice = a_list[2:4]
print(string_slice)
print(list_slice)

slice_from_beginning = a_list[:4]
slice_from_the_end = a_string[-10:]
print(slice_from_beginning)
print(slice_from_the_end)

every_other_word = a_list[:4:2]
reverse_list = a_list[::-1]
print(every_other_word)
print(reverse_list)

copy_of_a_list = a_list[:]
print(copy_of_a_list)

# Zero indexing and slices

print(len(a_list[2:5]) == 5 - 2)
print(a_list[:3] + a_list[3:]  == a_list)
print(len(a_list[:3]) == 3)

# Membership

print("characters" in a_string)
print("strings" in a_list)

# Concatenation

new_list = a_list + ["a", "few", "more", "items"]
print(new_list)
really_long_list = new_list * 100
print(really_long_list)

# Sequence operations

print(len(really_long_list))

list_of_numbers = [12, 4, 2, 27, 6, 4]
print(min(list_of_numbers))
print(max(list_of_numbers))
print(list_of_numbers.index(27))
print(list_of_numbers.count(4))

# Tuples

a_tuple = (1, 2, 3)
another_tuple = 1, 2, 3
one_more_tuple = (1, )
not_a_tuple = (1)

tuple_from_string = tuple("Make me a tuple")
print(tuple_from_string)
tuple_from_iterable = tuple(list_of_numbers)
print(tuple_from_iterable)

list_of_numbers[1] = 5
print(list_of_numbers)

# tuple_from_iterable[1] = 5  # this will raise a TypeError

# Don't use mutable objects as default function arguments. The function will reuse the same object each time it's called.

def function_that_builds_a_list(default_list=[]):
    default_list.append("New list item")
    return default_list

print(function_that_builds_a_list())
print(function_that_builds_a_list())

# Instead do this

def function_that_builds_a_list(default_list=None):
    if default_list is None:
        default_list = []
    default_list.append("New list item")
    return default_list

print(function_that_builds_a_list())
print(function_that_builds_a_list())

# Mutable sequence methods

shopping_list = ["Milk", "Peanut Butter", "Lettuce", "Bread", "Bananas"]

shopping_list.append("Cheese")
print(shopping_list)
shopping_list.insert(0, "Ice Cream")
print(shopping_list)
shopping_list.extend(["Apples", "Eggs"])
print(shopping_list)
shopping_list.pop()
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)
shopping_list.remove("Peanut Butter")
print(shopping_list)

# Modify in place with reverse and sort
shopping_list.reverse()
print(shopping_list)

shopping_list.sort()
print(shopping_list)

def sort_by_third_letter(string):
    return string[2]

shopping_list.sort(key=sort_by_third_letter)
print(shopping_list)

# Use slicing to delete and copy parts of a list or a whole list

del shopping_list[:2]
print(shopping_list)
new_shopping_list = shopping_list[2:]
print(new_shopping_list)

# Slicing makes a 'shallow copy', new list with the same objects. Mutable objects are mutated in both copies.

shopping_list = ["Milk", "Peanut Butter", ["Lettuce", "Bread", "Bananas"]]

copy_of_list = shopping_list[:]  # shallow copy
print(copy_of_list)
copy_of_list[2].pop()
print(copy_of_list)
print(shopping_list)

# Changing a list while iterating can lead to strange bugs

list_of_ten = list(range(10))
print(list_of_ten)

for item in list_of_ten:
    list_of_ten.remove(item)

print(list_of_ten)

# Iterate over a copy and modify the original instead

list_of_ten = list(range(10))
print(list_of_ten)

for item in list_of_ten[:]:
    list_of_ten.remove(item)

print(list_of_ten)
