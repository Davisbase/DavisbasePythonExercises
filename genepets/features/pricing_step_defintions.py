from lettuce import *

@step(u'a (.*) costs (.*)')
def given_pet_and_costs(context, pet, price):
    pass

@step(u'I enter (.*) and search for price')
def search_for_price(context, pet):
    pass

@step(u'the result should be (.*)')
def result(context, price):
    pass
