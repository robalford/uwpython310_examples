# Intro to Dictionaries

# Dict literal
my_dictionary = {
    "key": "value",
}

value = my_dictionary["key"]  # Keys as indexes

print(f"Retrieve values by using keys as indexes: {value}")

new_dict = dict()  # Dict construction
new_dict["key"] = "value"  # Value assignment

# Working with Dictionaries

# prints all the keys in order
print("Print all the keys:")
for k in my_dictionary:
    print(k)

# prints all the values in order
print("Print all the values:")
for v in my_dictionary.values():
    print(v)

# prints all the keys and values in order
print("Print keys and values:")
for k, v in my_dictionary.items():
    print(k, v)

# Dictionary Operations

if "key" in my_dictionary:
    print(f"Found key")

# will throw a KeyError
# key_error = my_dictionary["bad key"]

# returns None
key_not_found = my_dictionary.get("bad key")

# returns "default value" if "bad key" is not found
new_value = my_dictionary.get("bad key", "default value")

print(f"dict.get() can take an optional default return value: {new_value}")

# sets a value or creates new key / value pair if key does not exist
new_key_value = my_dictionary.setdefault("new key", "new value")

print(f"dict.setdefault() creates a new key-pair value if it doesn't exist:")
print(my_dictionary)

# More Dictionary Operations

new_dict = {
    2: "cat",
    1: "apple",
    3: "book",
}

# Use dict.update() to combine two dictionaries, overwriting values if keys exist
my_dictionary.update(new_dict)

print("Now my_dictionary is combined with new_dict:")
print(my_dictionary)

# Sorting

# Returns sorted keys
print("Use sorted to return sorted keys:")
sorted_keys = sorted(new_dict)
print(sorted_keys)

print("Use a key function to sort by values:")

def key_function(kv_tuple):
    return kv_tuple[1]

# dict.items() is list of tuples
sort_by_values = dict(
    sorted(new_dict.items(), key=key_function)
)

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

print("Called give_me_options(2):")

give_me_options(2)
