class TaxService:
    def calculate_tax(self, amount):
        """
        Imagine this has a lot of code with database calls, calls to other services, etc.

        You don't want your test to call it.

        But that terrible person that implemented the sales tax feature did the instantiation in your order service!
        """
        return None