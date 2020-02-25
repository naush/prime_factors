from unittest import TestCase
from prime_factors import PrimeFactors


class TestPrimeFactors(TestCase):

    def test_0(self):
        self.assertEquals([], PrimeFactors.of(0))

    def test_1(self):
        self.assertEquals([], PrimeFactors.of(1))

    def test_2(self):
        self.assertEquals([2], PrimeFactors.of(2))

    def test_4(self):
        self.assertEquals([2, 2], PrimeFactors.of(4))

    def test_3(self):
        self.assertEquals([3], PrimeFactors.of(3))

    def test_9(self):
        self.assertEquals([3, 3], PrimeFactors.of(9))

    def test_5(self):
        self.assertEquals([5], PrimeFactors.of(5))

    def test_25(self):
        self.assertEquals([5, 5], PrimeFactors.of(25))

    def test_a_very_large_prime_number(self):
        self.assertEquals([2, 3, 5, 7, 11, 13, 17], PrimeFactors.of(2*3*5*7*11*13*17))
