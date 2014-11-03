from nose.tools import *
from mock import MagicMock, patch, call
from mock_exercise.services.order_chips import OrderChipsFacade
from mock_exercise.external_services.credit_card_service import CreditCardService
from mock_exercise.external_services.chip_service import ChipService
from mock_exercise.external_services.tax_service import TaxService


class TestOrderChips:

    def test_happy_path_via_stubs(self):
        """
        Write a test that ensures that the right values are passed to the credit card and chip services.
        Implement this with a stub: make your own SUPER SIMPLE implementation of the two classes and pass those
         into the constructor.
        """

    def test_happy_path_via_monkey_patching(self):
        """
        Imagine that the chip price doesn't fluctuate, it's just a config value.  Mocking that is probably overkill.  Move
        that calculation (num_chips * price) into the actual chip service.

        Then, instead of re-creating it in your stub, monkey patch the other functions in the empty classes with functions
        defined here in your test.
        """

    def test_call_failure(self):
        """
        STOP -- Talk to instructor before starting this exercise.
        Now insert a bug by commenting out one of your calls to a monkey patched method.  Does your test fail?
        What if you called it twice instead of once?: It's hard for monkey patching to catch this without a
        lot of weird boilerplate code.

        Use magic mocks instead!  Follow the example below.
        """


    def test_patching_into_classes(self):
        """
        These mocks work well because we're doing dependency injection.  What if we don't?  Consider this scenario:

        After your beautifully test-driven-development code went into production, some other coder hacked in the sales
        tax solution.  Instead of doing TDD and DI, they just slapped in both the instantiation and the call to the sales
         tax service.  (go do that -- instantiate the sales tax service in the order_chips code)

        And now, you have to go back and make tests for it.  You don't want to change the constructor, but you need to fix all
        your tests.  Patch it in place!
        """
        tax_mock = MagicMock(spec=TaxService)  # Note that this is mocking the class instead of the method this time

        expected = call().calculate_tax(42).call_list()

        with (patch('mock_exercise.services.order_chips.TaxService',tax_mock)):
            pass
