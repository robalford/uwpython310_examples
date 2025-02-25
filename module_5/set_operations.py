# Set operators

set_1 = {1, 2, 3, 4, 5, 6, 7, 8}
set_2 = {2, 4, 6, 8, 10, 12, 14}
set_3 = {3, 5, 7}

set_1.add(2)
print(f"All set items are distinct:")
print(set_1)

set_3.update([7, 9, 11])
print(f"Add multiple items with set.update()")
print(set_3)

set_3.remove(9)
set_3.remove(11)
print("Use remove to remove specific values from the set:")
print(set_3)

# Set operators - uses operator overloading in Python like using + for addition or concatenation

# Union returns distinct elements from both sets
print(f"Set union: {set_1 | set_2}")

# Intersection returns distinct elements common to both sets
print(f"Set intersection: {set_1 & set_2}")

# Difference of set1 - set2 returns all elements in set1 but not set2
print(f"Set difference: {set_1 - set_2}")

# Subset determines if every element of one set is also in another
print(f"Set is subset: {set_3 <= set_1}")

# Superset determines if one set contains every element of another set
print(f"Set is superset: {set_1 >= set_3}")
