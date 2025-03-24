# One useful application of multiple inheritance in Python is the use of 'mix-in' classes

# These are classes that aren't intended to be used on their own, but rather to add specific
# attributes or behaviors to only certain subclasses

# Here is our original Contract class hierarchy

class Contract:
    def __init__(self, client, delivery_date):
        self.client = client
        self.delivery_date = delivery_date

    def __str__(self):
        return (f"Contract between {self.client} and Indie Software Development, LLC\n"
                f"Completed on: {self.delivery_date}")


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


# We can add an Annual Maintenance Mixin for subclasses that need to include an annual maintenance fee in their
# invoice.

# Mixins are not meant to be used on their own, but to add methods/behaviors that don't exist on other parent classes,
# and are only needed in certain classes in the hierarchy.

class AnnualMaintenanceMixin:
    @staticmethod
    def calculate_maintenance_costs(annual_hosting_costs, total_contract_value):
        return annual_hosting_costs + total_contract_value * .2


class HourlyWithMaintenance(AnnualMaintenanceMixin, HourlyContract):
    def __init__(self, annual_hosting_costs, *args):  # Use *args for parent class arguments
        super().__init__(*args)
        self.annual_hosting_costs = annual_hosting_costs

    def display_invoice_amount(self):
        invoice_amount = super().display_invoice_amount()
        annual_maintenance_costs = self.calculate_maintenance_costs(self.annual_hosting_costs, self.total_amount_due)
        return (f"{invoice_amount} \n"
                f"Annual maintenance: {annual_maintenance_costs} \n"
                f"Total amount due: {self.total_amount_due + annual_maintenance_costs}")


print("\n")
contract1 = HourlyWithMaintenance(120, "Acme Design Studios", "2/27/25", 50, 80)
print(contract1)
print("\n")
print(contract1.display_invoice_amount())
print("\n")
