import unittest
from Module1 import is_prime
#from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertFalse(is_prime(-5000))
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(-100))

    def test_zero_and_one(self):
        self.assertEqual(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_small_composites(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_large_primes(self):
        self.assertTrue(is_prime(103))
        self.assertTrue(is_prime(107))
        self.assertTrue(is_prime(109))

    def test_large_composites(self):
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(200))
        self.assertFalse(is_prime(300))

#unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    unittest.main()
