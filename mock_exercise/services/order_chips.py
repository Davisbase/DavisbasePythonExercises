from mock_exercise.external_services.tax_service import TaxService

class OrderChipsFacade:
    def __init__(self, chip_service, credit_card_service):
        self._chip_service = chip_service
        self._credit_card_service = credit_card_service

    def order_chips(self, credit_card_number, account_number, num_chips):
        """
        This is the code we want to write!  It should make use of the two services in the services.py module,
        presenting them as a single interface.

        This method should debit the user's credit card for the right amount, and add the chips to the player's
        account.
        """
        pass
