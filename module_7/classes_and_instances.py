# A class is a category of objects with shared characteristics and behavior. They can be used to model real world things
# and situations.

class Book:
    # In Python a class's __init__() method is used to define instance attributes and instantiate new objects.
    # This method is called when the instance object is created, and used to pass in specific traits or data for that
    # particular object.
    def __init__(self, title, author):  # self is required as the first parameter, and refers to the object instance
        self.title = title
        self.author = author


# An instance is a particular object with specific traits. You pass in attribute values defined in the __init__()
# method to instantiate a new object. But you don't pass in self, because it always gets passed in automatically
# as the first parameter of a method

pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")

# Then you can access the object's attributes using dot notation, like variables that belong to the object.

# print(f"Book title: {pride_and_prejudice.title}")
# print(f"Book author: {pride_and_prejudice.author}")
