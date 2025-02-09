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

slice_from_beginning = a_list[:4]
slice_from_the_end = a_string[-10:]

every_other_word = a_list[:4:2]
reverse_list = a_list[::-1]

copy_of_a_list = a_list[:]

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
tuple_from_iterable = tuple(list_of_numbers)

list_of_numbers[1] = 5
print(list_of_numbers)

# tuple_from_iterable[1] = 5  # this will raise a TypeError

