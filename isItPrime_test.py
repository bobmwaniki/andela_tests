import unittest

class PrimeNumberTester(unittest.TestCase):

	def test_output(self):
		# primes
		self.assertTrue(isItPrime(5), msg='5 is prime and function should return True')
		self.assertTrue(isItPrime(43), msg='43 is prime and function should return True')
		self.assertTrue(isItPrime(929), msg='929 is prime and function should return True')
		# non primes
		self.assertFalse(isItPrime(4), msg= '4 is not prime. Should return False')
		self.assertFalse(isItPrime(90), msg= '90 is not prime. Should return False')
		self.assertFalse(isItPrime(600), msg= '600 is not prime. Should return False')


if __name__ == '__main__':
	unittest.main()
