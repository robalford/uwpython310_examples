from textwrap import dedent

# Object Composition in Python

# Let's explore the difference between inheritance and composition in OOP by continuing work on our
# invoicing system for Indie Software Development, LLC

# We'll start by defining a new Invoice class for generating invoices to send to clients for payment. But to create
# an invoice, and send it in the mail we also need to keep track of our clients' addresses.

# In the previous version of our program the client was included as a string field on the Contract class. So we could
# list out address fields there, but this would tightly couple the client and contract data in our program and lead
# to duplication if we had multiple contracts for the same client.

# Instead, let's create a new Client class that can contain the client's name, address and any other data that we
# want to track. This is a better way of encapsulating related data and behavior in a single class.


class Client:
    def __init__(self, business_name, business_address):
        self.business_name = business_name
        self.business_address = business_address

    def __str__(self):
        return (f"Client: {self.business_name}\n"
                f"Address:{self.business_address}")


# We can then use composition to reference a Client object instance in our Contract class. Whereas inheritance can be
# used to represent an 'is a' relationship between objects, composition is the better choice for 'has a' relationships.

# In this program, an HourlyContract 'is a' 'Contract', but a 'Contract' has a 'Client' associated with it.

class Contract:
    def __init__(self, client, delivery_date):
        self.client = client  # this is now a reference to a Client instance
        self.delivery_date = delivery_date

    def __str__(self):
        return (f"Contract between {self.client.business_name} and Indie Software Development, LLC\n"
                f"Completed on: {self.delivery_date}")


# Our subclass code stays the same in this version

class HourlyContract(Contract):
    def __init__(self, client, delivery_date, hourly_rate, total_hours_worked):
        super().__init__(client, delivery_date)
        self.hourly_rate = hourly_rate
        self.total_hours_worked = total_hours_worked

    @property
    def total_amount_due(self):
        return self.hourly_rate * self.total_hours_worked

    def display_invoice_amount(self):
        """Generate a string to display total amount due on an invoice."""
        return f"{self.total_hours_worked} total hours x {self.hourly_rate}/hour = {self.total_amount_due}"


class FixedBidContract(Contract):
    def __init__(self, client, delivery_date, bid_amount):
        super().__init__(client, delivery_date)
        self.bid_amount = bid_amount

    def display_invoice_amount(self):
        return f"Total amount due: {self.bid_amount}"


# Now we can create a new Invoice class for generating invoices to send to clients for payment. This class also
# uses composition instead of inheritance where each Invoice object 'has a' Contract object associated with it.
# Because invoices and contracts are different document types used for different purposes, it is better not to
# tightly couple their logic and behavior through inheritance and practice clean separation of concerns.

class Invoice:
    def __init__(self, invoice_number, contract):
        self.invoice_number = invoice_number
        self.contract = contract

    # Now we can generate invoices for different Contract subclasses as long as they define a display_invoice_amount()
    # method. And the Invoice class doesn't need to know what's going on 'under the hood' to calculate those amounts.
    def generate_invoice(self):
        print(dedent(f"""
            Indie Software Development, LLC
            Invoice number: {self.invoice_number}
            
            Client: {self.contract.client.business_name}
            Address: {self.contract.client.business_address}
        
            Work completed on: {self.contract.delivery_date}
            {self.contract.display_invoice_amount()}
        """)
        )


# Now to test our invoicing system, let's instantiate a couple new Client objects

client1 = Client("Acme Design Studios", "123 Brooklyn Street Seattle WA 98105")
client2 = Client("E-commerce Extravaganza", "999 Meridian Ave Shoreline WA 98133")

# And we'll create a few Contract objects for these clients

contract1 = HourlyContract(client1, "2/27/25", 50, 80)
contract2 = FixedBidContract(client2, "3/15/25", 2500)
contract3 = FixedBidContract(client1, "3/22/25", 500)

# Then we can generate invoices for each of these contracts with our Invoice objects with different Contract types

invoice1 = Invoice("12345", contract1)
invoice2 = Invoice("12346", contract2)
invoice3 = Invoice("12347", contract3)

invoice1.generate_invoice()
print("\n")
invoice2.generate_invoice()
print("\n")
invoice3.generate_invoice()
print("\n")
