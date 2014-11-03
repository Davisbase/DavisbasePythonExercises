"""
This is one of the external service calls that we want to mock.

For this exercise, assume that a real call will take too long,
and won't be ready for a long time.
"""

class ChipService:
    def add_chips(self, account_number, chips):
        pass

    def get_chip_price(self, num_chips):
        pass
