import unittest
import primes
import math
from nose.tools import assert_equals, assert_true, assert_false

class TestPrimes:

    known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29];

    def test_get_primes_up_to_one(self):
        primes_result = primes.PrimesMaker.get_primes(1)
        assert_equals([], primes_result)

    def test_generate_primes_up_to_one(self):
        primes_result = primes.generate_primes(1)
        assert_equals([], list(primes_result))

    def test_get_primes_up_to_five(self):
        primes_result = primes.PrimesMaker.get_primes(5)
        expected_result = [2, 3, 5]
        assert_equals(expected_result, primes_result)

    def test_get_primes_up_to_thirty(self):
        primes_result = primes.PrimesMaker.get_primes(30)
        assert_equals(self.known_primes, primes_result)

    def test_generate_primes_up_to_thirty(self):
        primes_result = list(primes.generate_primes(30))
        assert_equals(self.known_primes, primes_result)

    def test_get_lots_has_all_primes(self):
        lots_of_primes = primes.PrimesMaker.get_primes(10000)
        non_primes = []
        for candidate in lots_of_primes:
            if not _prime(candidate):
                non_primes.append(candidate)

        assert_equals([], non_primes)

    def test_generate_lots_has_all_primes(self):
        non_primes = []
        for candidate in list(primes.generate_primes(10000)):
            if not _prime(candidate):
                non_primes.append(candidate)

        assert_equals([], non_primes)

def _prime(candidate):
    if candidate < 2:
        return True

    result = True
    check_boundary = candidate #math.sqrt(candidate)
    divisor = 2
    while (result and divisor < check_boundary):
        result = (0 != candidate % divisor)
        divisor += 1

    return result