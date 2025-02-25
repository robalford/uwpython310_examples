# Set operators

set_1 = {1, 2, 3, 4, 5, 6, 7, 8}
set_2 = {2, 4, 6, 8, 10, 12, 14}
set_3 = {3, 5, 7}

# Union returns distinct elements in either set
print(f"Set union: {set_1 | set_2}")

# Intersection returns distinct elements common to both sets
print(f"Set intersection: {set_1 & set_2}")

# Difference of set1 - set2 returns all elements in set1 but not set2
print(f"Set difference: {set_1 - set_2}")

# Subset determines if every element of one set is also in another
print(f"Set is subset: {set_3 <= set_1}")

# Superset determines if one set contains every element of another set
print(f"Set is superset: {set_1 >= set_3}")
