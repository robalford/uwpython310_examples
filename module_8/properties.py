import requests

# Using properties for getters and setters in Python


# In Python all object attributes are considered public by default.

class MyClass:
    def __init__(self, my_attribute):
        self.my_attribute = my_attribute


instance = MyClass("Hello")
# print(instance.my_attribute)

# Any code that uses this class instance can change its attribute values on the fly.

instance.my_attribute = "Hi there"
# print(instance.my_attribute)


# Many Object-oriented programming languages encourage (and enforce) the use of private attributes
# that can only be accessed and set through getter and setter methods.

class MyClass:
    def __init__(self, private_attribute):
        # The leading underscore indicates a private attribute. In Java and other object-oriented languages, this
        # is enforced. In Python, it is used as a convention to indicate that an attribute should be considered private.
        self._private_attribute = private_attribute

    def set_private_attribute(self, attribute_value):
        # Perform some validation logic here
        self._private_attribute = attribute_value

    def get_private_attribute(self):
        # Add calculations or other processing here
        return self._private_attribute


# The reason for this is that if you need to add some validation or other logic at a later point when an attribute
# is created or retrieved, you can extend your class in this way without impacting other code that gets or sets
# the attribute values elsewhere. But it makes your code more verbose.

instance = MyClass("Private attribute value")
# print(instance.get_private_attribute())
instance.set_private_attribute("New private attribute value")
# print(instance.get_private_attribute())


# In Python, you have the option of implementing a similar pattern using @properties for getters and setters. Or you
# can choose to allow direct attribute access depending on your program's design and how the objects will be used.

class MyClass:
    def __init__(self, private_attribute):
        self._private_attribute = private_attribute

    # The @ symbol creates a decorator in Python, which is a language feature that adds some pre-defined functionality
    # to a function or method. You'll learn more about them later in the certificate course. Here we are using the
    # @property decorator to create a property value that can be accessed using dot notion just like other
    # attributes (instead of calling the method that creates them).
    @property
    def private_attribute(self):
        return self._private_attribute

    @private_attribute.setter
    def private_attribute(self, attribute_value):
        # Now we can add validation logic or other code here as needed
        print("I'm doing something important here!")
        self._private_attribute = attribute_value


# The Python properties syntax is much more concise and allows you to access private attributes directly with dot
# notation (you don't call them with parentheses). So they look like attributes on the instance, but can implement
# additional logic and behavior like methods

instance = MyClass("Private attribute value")
# print(instance.private_attribute)

# Setters can be used to do some extra work when attribute values are set

# instance.private_attribute = "New private attribute value"
# print(instance.private_attribute)


# If you don't define a setter, you can create 'read only' attributes. And you can add a 'deleter' if you need to be
# able to delete the attribute.

class MyClass:
    def __init__(self, read_only_attribute):
        self._read_only_attribute = read_only_attribute

    @property
    def read_only_attribute(self):
        return self._read_only_attribute

    @read_only_attribute.deleter
    def read_only_attribute(self):
        print("Deleting read-only attribute..")
        del self._read_only_attribute


instance = MyClass("Read only value")
# instance.read_only_attribute = "New value"  # this will throw an attribute error

# del instance.read_only_attribute  # can't be deleted without implementing a deleter (and usually shouldn't be)


# Properties can also be used for caching attribute values, that are 'expensive' or resource-intensive to compute.
# The following example is adapted from the book 'Python 3 Object Oriented Programming by Dusty Phillips'
# (a good read if you want to go deeper into OOP with Python).

class WebPage:
    def __init__(self, url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print("Getting web page..")
            self._content = requests.get(self.url).text
        return self._content


# Now this class will only request the web page the first time the content attribute is accessed, and return the
# cached value after that

wikipedia = "https://www.wikipedia.org"
webpage = WebPage(wikipedia)

# content1 = webpage.content  # This time we make an HTTP request
# content2 = webpage.content  # This time we return the cached value

# print(content2)


# Python properties also provide a nice syntax for attribute values that need to be calculated at the time they
# are accessed, or that depend on the values of other object attributes

class Numbers:
    def __init__(self, numbers_list):
        self.numbers_list = numbers_list

    @property
    def average(self):
        return sum(self.numbers_list) / len(self.numbers_list)


my_numbers = Numbers([0, 5, 10])

# Properties let you access calculated values just like other attribute values. This is more concise and readable than
# using a calculate_average() method.
print(my_numbers.average)
