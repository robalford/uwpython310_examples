from inheritance import HourlyContract

# One useful application of multiple inheritance in Python is the use of 'mix-in' classes

# Mixins are not meant to be used on their own, but to add methods/behaviors that don't exist on other parent classes,
# and are only needed in certain classes in the hierarchy.

# We can add an Annual Maintenance Mixin for subclasses that need to include an annual maintenance fee in their
# invoice.


class AnnualMaintenanceMixin:
    @staticmethod
    def calculate_maintenance_costs(annual_hosting_costs, total_contract_value):
        return annual_hosting_costs + total_contract_value * .2


class HourlyWithMaintenance(AnnualMaintenanceMixin, HourlyContract):
    # Using *args for parent class attributes is a common pattern as inheritance hierarchies grow
    def __init__(self, annual_hosting_costs, *args):
        super().__init__(*args)
        self.annual_hosting_costs = annual_hosting_costs

    def display_invoice_amount(self):
        # super().display_invoice_amount() calls the method defined on HourlyContract
        invoice_amount = super().display_invoice_amount()
        # self.calculate_maintenance_costs() is inherited from AnnualMaintenanceMixin
        annual_maintenance_costs = self.calculate_maintenance_costs(
            self.annual_hosting_costs, self.total_amount_due
        )
        return (f"{invoice_amount} \n"
                f"Annual maintenance: {int(annual_maintenance_costs)} \n"
                f"Total amount due: {int(self.total_amount_due + annual_maintenance_costs)}")


if __name__ == "__main__":
    print("\n")
    contract1 = HourlyWithMaintenance(120, "Acme Design Studios", "2/27/25", 50, 80)
    print(contract1)  # This uses the __str__() method from the base Contract class
    print("\n")
    print(contract1.display_invoice_amount())  # This uses the display_invoice_amount() method from the current instance
    print("\n")
