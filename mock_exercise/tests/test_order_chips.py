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
        stub_card_service = StubCreditCardService()
        stub_chip_service = StubChipServices(1)
        order_service = OrderChipsFacade(stub_chip_service, stub_card_service)

        card_number = "1234 1235 1236 1237"
        acct_number = "9392832032"
        num_chips = 100
        order_service.order_chips(card_number, acct_number, num_chips)
        assert_equals(stub_card_service.received_card_number, card_number)

    def test_happy_path_via_monkey_patching(self):
        """
        Imagine that the chip price doesn't fluctuate, it's just a config value.  Mocking that is probably overkill.  Move
        that calculation (num_chips * price) into the actual chip service.

        Then, instead of re-creating it in your stub, monkey patch the other functions in the empty classes with functions
        defined here in your test.
        """
        expected_card_number="5555 3333 2222 1111"
        expected_amount=42
        dict_flag = {'wasCalled':False} # get around variable binding with a dict

        def take_money_monkey(self, card_number, amount):
            assert_equals(expected_card_number, card_number)
            assert_equals(expected_amount, amount)
            dict_flag['wasCalled']=True

        # nose creates an instance per test -- if you don't use nose, you have to put the original function back!
        CreditCardService.take_money = take_money_monkey
        card_service = CreditCardService()
        order_service = OrderChipsFacade(ChipService(), card_service)
        order_service.order_chips(expected_card_number, None, None)
        assert_equals(True, dict_flag['wasCalled'])

    def test_call_failure(self):
        """
        STOP -- Talk to instructor before starting this exercise.
        Now insert a bug by commenting out one of your calls to a monkey patched method.  Does your test fail?
        What if you called it twice instead of once?: It's hard for monkey patching to catch this without a
        lot of weird boilerplate code.

        Use magic mocks instead!  Follow the example below.
        """

        #arrange
        expected_card_number="5555 3333 2222 1111"
        expected_amount=42
        take_money_mock = MagicMock(spec=CreditCardService.take_money)()
        CreditCardService.take_money = take_money_mock
        card_service = CreditCardService()
        order_service = OrderChipsFacade(ChipService(), card_service)

        #act
        order_service.order_chips(expected_card_number, None, None)

        #assert
        take_money_mock.assert_called_with(expected_card_number, expected_amount)

    # @patch('mock_exercise.services.order_chips.OrderChipsFacade.TaxService',tax_mock)
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
            take_money_mock = MagicMock(spec=CreditCardService.take_money)()
            CreditCardService.take_money = take_money_mock
            card_service = CreditCardService()
            order_service = OrderChipsFacade(ChipService(), card_service)
            order_service.order_chips(None, None, None)

        # tax_mock.assert_called_with() #the constructor
        assert_in(expected, tax_mock.mock_calls)


class StubCreditCardService:
    def __init__(self):
        self.received_card_number=None
        self.received_amount=None

    def take_money(self, card_number, amount):
        self.received_card_number = card_number
        self.received_amount = amount

class StubChipServices:
    def __init__(self, price):
        self._price = price
        self.received_account_number=None
        self.received_chips=None

    def add_chips(self, account_number, chips):
        self.received_account_number = account_number
        self.received_chips = chips

    def get_chip_total_cost(self, num_chips):
        return price * num_chips
