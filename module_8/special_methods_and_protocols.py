from functools import total_ordering


# Duck typing in Python - "If it walks like a duck, and it quacks like a duck, then it must be a duck"

# Objects of different classes can be used in the same way if they implement the same attributes and methods

class Duck:
    def fly(self):
        print("The duck is flying.")


class Goose:
    def fly(self):
        print("The goose is flying.")


class Hawk:
    def fly(self):
        print("The hawk is flying.")


# As long as a class implements a fly method, it can be treated as a bird without needing to check its type in the
# code. Classes that share the same interface can be used in the same ways - this is what duck typing means.

birds = [Duck(), Goose(), Hawk()]

# for bird in birds:
#     bird.fly()


# Python types use special methods with double underscores (aka magic methods or dunder methods) to create protocols
# so that you can implement the same methods in your classes to make them behave like built-in types

# You can view all of an object's special methods by calling dir(object)

# print(dir(2))  # The Numeric Protocol
# print(dir(list))  # The Container Protocol

# You don't have to implement all the methods for a specific protocol, you can just implement the ones you
# need for your classes.


# Example of using magic methods to implement a Square class that can be used with mathematical and comparison
# operators

@total_ordering
class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side * self.side

    # Implement the __str__() method to print a readable representation of the object
    def __str__(self):
        return f"Area of square: {self.area}"

    # Implement the __repr__() method to provide an 'official' string representation of the object - used with repr()
    # and in the Python console. Representation in the context of your program for error messages etc.
    def __repr__(self):
        return f"Square({self.side})"

    # Implement the __add__() method to create a new square object by adding two square objects with the + operator.
    def __add__(self, other):
        return Square(self.side + other.side)

    # The functools.total_ordering decorator lets you implement comparison between objects by defining just the
    # __eq__() and __lt__() methods.
    def __eq__(self, other):
        return self.side == other.side

    def __lt__(self, other):
        return self.side < other.side


square1 = Square(5)
square2 = Square(7)

# print(square1)
# print(square2)

# Because we implemented the __add__() method, we can use the '+' operator to add two Square instances. This is
# known as 'operator overloading' in Python which means that operators can behave differently depending on what types
# are using them

square3 = square1 + square2

# print(f"Square 3 side length: {square3.side}")
# print(square3)

# We can compare Square objects using the comparison operators because we implemented the __eq__() and __lt__()
# methods using the @total_ordering decorator

# print(square1 == square2)
# print(square3 < square2)
# print(square1 == Square(5))
# print(square1 >= Square(5))

# Python uses the __lt__() method for sorting objects, so if you want your objects to be sortable you need to
# implement __lt__()

squares = [square3, square1, square2]

print(squares)
print(sorted(squares))  # uses our __repr__() to represent the objects in the console output
print(sorted(squares, reverse=True))


# You can use the __call__() method to create object instances that can be called like functions

# Example below adapted from:
# https://realpython.com/python-callable-instances/#creating-callable-instances-with-__call__-in-python

class PowerFactory:
    def __init__(self, exponent):
        self.exponent = exponent

    def __call__(self, base):
        return base**self.exponent


square_of = PowerFactory(2)
print(square_of(3))
print(square_of(6))

cube_of = PowerFactory(3)
print(cube_of(3))
print(cube_of(5))
