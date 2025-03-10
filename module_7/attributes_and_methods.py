# Attributes and methods

class Book:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.pages_read = 0  # You can set initial attribute values for all instances
        self.finished_book = False

    # Custom methods

    def read_to_page(self, page_number):
        self.pages_read = page_number  # Methods can update instance attribute values
        print(f"Read to page {page_number} of {self.title} by {self.author}")
        if page_number >= self.number_of_pages:
            self.finish_book()  # And they can call other methods of the object

    def finish_book(self):
        self.finished_book = True
        print(f"You finished {self.title} by {self.author}")

    def pages_left_to_read(self):
        return self.number_of_pages - self.pages_read


moby_dick = Book("Moby Dick", "Herman Melville", 635)

# print(f"Title: {moby_dick.title}")
# print(f"Author: {moby_dick.author}")
# print(f"Number of pages: {moby_dick.number_of_pages}")
# # All new Book instances begin with zero pages read
# print(f"Pages read: {moby_dick.pages_read}")


# When you call methods, the object instance gets automatically passed in as the first argument. Methods can return
# new values or objects.

# moby_dick.read_to_page(100)
# print(moby_dick.pages_read)
# print(f"You have {moby_dick.pages_left_to_read()} pages left to read.")

# You can also update instance attribute values directly with assignment.

# moby_dick.pages_read = 200
# print(f"Pages read: {moby_dick.pages_read}")
# print(f"You have {moby_dick.pages_left_to_read()} pages left to read.")

# Encapsulation means the details of the data structure and internal object behavior do not need to be known in order
# to use the object. If we read to the last page, the Book.finish_book() method is called internally indicating that
# we've completed the book.

# moby_dick.read_to_page(635)


# You can also define class attributes that are shared between all instances of a class.

class Car:
    number_of_wheels = 4

    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color


car = Car("Subaru", "Outback", "Black")
car2 = Car("Ford", "Explorer", "Green")

# print(f"I just bought a new {car.color} {car.make} {car.model} and it has {car.number_of_wheels} wheels!")
# print(f"I just bought a new {car2.color} {car2.make} {car2.model} and it has {car2.number_of_wheels} wheels!")
