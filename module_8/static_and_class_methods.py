# Static methods can be used when you don't need to work with the object instance in a method.


class MyClass:
    # Use the @staticmethod decorator on a method if you don't need the self argument that refers to the object
    # instance in the method.
    @staticmethod
    def my_static_method():
        print("I'm static.")


instance = MyClass()
# instance.my_static_method()

# Why would you do this? Why not just use a module-level function? Usually you should just use a function. But
# sometimes it makes sense for some action or behavior to live inside a class, even though it doesn't work directly
# with instance attribute data.

# Class methods are methods that take the class object as an argument rather than an instance object. This can be useful
# for providing alternate initializer methods in your classes. Like in the 'factory pattern' below where classes can
# create their own instances with predefined attribute data.


class Sandwich:
    # Users of this class can create their own custom sandwiches
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    # Or they can use alternate constructors (or factory functions) to create some tried and true combos

    @classmethod
    def reuben(cls):
        return cls("Reuben", ["Rye bread", "Corned beef", "Sourkraut", "Swiss", "Thousand Island"])

    @classmethod
    def blt(cls):
        return cls("BLT", ["Sourdough", "Lettuce", "Tomato", "Bacon", "Mayo"])

    def print_sandwich(self):
        print(self.name)
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")


custom_sandwich = Sandwich("Kimchi Grilled Cheese", ["Sourdough", "Cheddar", "Kimchi", "Mayonnaise"])
custom_sandwich.print_sandwich()

reuben = Sandwich.reuben()
reuben.print_sandwich()

blt = Sandwich.blt()
blt.print_sandwich()
