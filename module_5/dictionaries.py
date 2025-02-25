# Intro to Dictionaries

# Dict literal
my_dictionary = {
    "key": "value",
}

value = my_dictionary["key"]  # Keys as indexes

new_dict = dict()  # Dict construction
new_dict["key"] = "value"  # Value assignment

# Working with Dictionaries

# prints all the keys in order
for k in my_dictionary:
    print(k)

# prints all the values in order
for v in my_dictionary.values():
    print(v)

# prints all the keys and values in order
for k, v in my_dictionary.items():
    print(k, v)

# Dictionary Operations

if "key" in my_dictionary:
    print("Found key")

# will throw a KeyError
# key_error = my_dictionary["new key"]

# returns None
key_not_found = my_dictionary.get("bad key")

# returns "new value" if "bad key" is not found
new_value = my_dictionary.get("bad key", "default value")

# creates new key / value pair
new_key_value = my_dictionary.setdefault(
    "new key", "new value"
)

# Dictionary Sorted

unsorted_dict = {
    2: "cat",
    1: "apple",
    3: "book",
}

# Returns sorted keys
sorted_keys = sorted(unsorted_dict)

def key_function(kv_tuple):
    return kv_tuple[1]

# dict.items() is list of tuples
sort_by_values = dict(
    sorted(unsorted_dict.items(), key=key_function)
)

print(sorted_keys)
print(sort_by_values)

# Match / Case

def give_me_options(option):
    match option:
        case 1:
            print("Do something with 1")
        case 2:
            print("Do something with 2")
        case _:
            print("Do something with anything else")

give_me_options(2)
