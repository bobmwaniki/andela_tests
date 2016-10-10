import unittest

class FibonacciTest(object):
	"""docstring for FibonacciTest"""
	def test_length(self):
		self.assertEqual(len(fibonachi_sequence(5)), 5, msg= 'The list should have 5 elements')

	def test_output_list(self):
		self.assertEqual(fibonachi_sequence(6), [1,1,2,3,5,8], msg='The list does not contain 6 elements of the Fibonacci sequence in order')

if __name__ == '__name__':
	unittest.main()
