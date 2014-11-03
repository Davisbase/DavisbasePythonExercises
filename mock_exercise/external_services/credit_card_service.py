"""
This is one of the external service calls that we want to mock.

For this exercise, assume that a real call will take too long time,
and won't be ready for a long time.
"""
class CreditCardService:
    def take_money(self, card_number, amount):
        pass