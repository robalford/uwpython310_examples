# Strings

# Create string literal with single, double or triple quotes

string1 = 'I am a string'
string2 = "So am I"
string3 = """I am
a multi-line
string"""

print(string1)
print(string2)
print(string3)

# Make a string out of a different data type with str

print(str(23))
print(type(str(23)))

# Splitting and joining strings

comma_separated_values = "1,2,3,4"

list_from_comma_separated_values = comma_separated_values.split(",")
print(list_from_comma_separated_values)

pipe_separated_values = "|".join(list_from_comma_separated_values)
print(pipe_separated_values)

# Other handy string methods

print("make me upper".upper())
print("MAKE ME LOWER".lower())
print("a book title".title())
print("23".isalpha())
print("23".isnumeric())

# Escape special characters

lots_of_lines = "I \nam \na \nstring \nwith \nmany \nline \nbreaks"
print(lots_of_lines)

preserve_backslashes = r"I\like\backslashes"
print(preserve_backslashes)

# Python joins adjacent strings

print("If you don't use"
      " a new line character"
      " Python will join strings together")

# String Formatting

# Ways to join strings with other data

name = "Rob"
the_bad_way = "Hello " + name + "!"
the_old_way = "Hello %s!" % name
the_better_way = "Hello {}!".format(name)
the_fstring_way = f"Hello {name}!"  # the best way?

print(the_bad_way)
print(the_old_way)
print(the_better_way)
print(the_fstring_way)

# fstrings are concise and readable and allow you to interpolate expressions into strings

two_plus_two = f"2 + 2 = {2 + 2}"
print(two_plus_two)

