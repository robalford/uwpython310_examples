# Object Inheritance in Python

# Let's build an invoicing system for a freelance software development company to
# learn about inheritance, composition and other Object-oriented programming concepts
# in Python

# Inheritance allows you to reuse the code of existing classes by creating subclasses

# Our company "Indie Software Development, LLC" needs to create invoices for different
# types of contracts: hourly contracts and fixed bid contracts

# We can model these contract types in our program as Python classes and use
# inheritance to reuse code from a base class called Contract

class Contract:
    def __init__(self, client, delivery_date):
        self.client = client
        self.delivery_date = delivery_date

    def __str__(self):
        return (f"Contract between {self.client} and Indie Software Development, LLC\n"
                f"Completed on: {self.delivery_date}")


# All contracts have a client and delivery date, so we set those as attributes in our
# base class's __init__() method and then use inheritance to pass those attributes
# down to multiple subclasses

# In Python, you inherit from a base class by passing it into parentheses in the
# first line of your subclass definition

class HourlyContract(Contract):
    # Now we can override methods from the base class to add additional functionality
    def __init__(self, client, delivery_date, hourly_rate, total_hours_worked):
        # And we can call methods on the base class with super()
        super().__init__(client, delivery_date)
        # And we can extend the base class by adding new attributes and methods
        self.hourly_rate = hourly_rate
        self.total_hours_worked = total_hours_worked

    # We use a property for the total_amount_due calculated value
    @property
    def total_amount_due(self):
        return self.hourly_rate * self.total_hours_worked

    # And define a new display_invoice_method that can be implemented differently for
    # different subclasses of Contract
    def display_invoice_amount(self):
        """Generate a string to display total amount due on an invoice."""
        return f"{self.total_hours_worked} total hours x {self.hourly_rate}/hour = {self.total_amount_due}"


# We can use the same techniques to create a different subclass for a FixedBidContract
# subclass, with attributes and methods specific to that type of contract

class FixedBidContract(Contract):
    def __init__(self, client, delivery_date, bid_amount):
        super().__init__(client, delivery_date)
        self.bid_amount = bid_amount

    def display_invoice_amount(self):
        return f"Total amount due: {self.bid_amount}"


# Now when we instantiate our subclasses, we have access to the attributes and
# methods defined on their base class as well

contract1 = HourlyContract("Acme Design Studios", "2/27/25",
                           50, 80)

contract2 = FixedBidContract("E-commerce Extravaganza", "3/15/25",
                             2500)

print("\n")
print(contract1)
print(contract1.display_invoice_amount())
print("\n")
print(contract2)
print(contract2.display_invoice_amount())
print("\n")
