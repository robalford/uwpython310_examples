# Multiple Inheritance in Python

# Python supports multiple inheritance, but it should be used sparingly as complicated class hierarchies
# quickly become difficult to maintain

# When Python looks for a method or attribute, it searches from bottom to top in the current class, then
# from left to right in super classes listed in class definition

# This is what's meant by 'method resolution order' or MRO, and it's determined at runtime when you call
# super().method() inside a subclass

# This is Python's way of solving the 'diamond problem' where you have two super classes that both implement the
# same method

# See the following example of Python's MRO in multiple inheritance adapted from Stack Overflow:
# https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance

class First:
    def __init__(self):
        print("first")


class Second(First):
    def __init__(self):
        print("second")


class Third(First):
    def __init__(self):
        print("third")


class Fourth(Second, Third):
    def __init__(self):
        super().__init__()
        print("that's it")

# In this example, the MRO would be [Fourth, Second, Third, First].


# Here's the output of instantiating Fourth. And you can change it by adding super().__init__() calls to the
# other classes and Python will look left to right and then up to superclasses for methods to call. You can
# see how this gets complicated quickly. So use multiple inheritance sparingly.

f = Fourth()
