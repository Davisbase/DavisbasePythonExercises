import unittest
from nose.tools import assert_equals

class TestYourSetup:

    def passing_test_example(self):
        myList = [1, 2, 3, 4, 5]
        assert_equals(len(myList), 5, "wrong length value")

    def failing_test_example(self):
        whole_name = 'Kris' + 'Kringle'
        assert_equals(whole_name, 'Kris Kringle')

class TestSetupExample:

	def setUp(self):
		# setup a dictionary of winning throw : beaten throw
		self.rps = {'Rock':'Scissors', 'Paper':'Rock', 'Scissors':'Paper'}

	def test_bomb_expansion(self):
		self.rps['Bomb']='Rock'
		self.rps['Bomb']='Paper'
		self.rps['Scissors']=['Paper','Bomb']

		assert_equals(len(self.rps.keys()), 4)

class TestSkippy:

	@unittest.skip("Ain't nobody got time for that")
	def superLongRunningTest(self):
		time.sleep(500)