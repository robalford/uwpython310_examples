# In Python everything is an object of a certain type.

# There are many built-in types.

print(type("I'm a string"))
print(type(25))
print(type(False))
print(type([]))


# A class statement creates a new custom type.

class MyClass:
    pass


# print(type(MyClass))

# A type is just a special kind of object in Python, with shared attributes and methods that can be useful when
# creating other custom objects.

# A class is a 'subclass' of object in Python, and it inherits these attributes and methods from its parent class.

# print(issubclass(MyClass, object))
# print(dir(MyClass))

# The built-in types we've been using also inherit from object and have the same attributes and methods, as well as
# their own custom methods for defining their unique data and behavior.

# print(issubclass(list, object))
# print(dir(list))

# We've been using these custom methods for built-in types like lists and strings. Methods are just functions that
# belong to an object and are called from the object's namespace using dot notation and parentheses.

some_words = "some words"
# print(some_words.upper())


# When you define a class in Python, you create a new custom type with its own attributes and methods that you
# can access and use in the same way as the built-in types.

class CustomType:
    custom_attribute = "My first attribute"

    # More on this self thing later ...
    def custom_method(self):
        print("Methods are like functions that work with class attributes.")
        print(f"My attribute: {self.custom_attribute}")


# When you create a new instance of a class object by calling it with parentheses, the instance's type
# is the custom class, and you can access its attributes and methods with dot notation.

c = CustomType()

# print(type(c))
# c.custom_method()
