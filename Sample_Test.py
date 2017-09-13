import unittest

def subtract_one(inp_integer):
	return inp_integer-1

class FunctionTests(unittest.TestCase):
	def setUp(self):
		pass

	def test_subt_function(self):
		self.assertEqual(subtract_one(3),2,"testing if subtract function works")
	def tearDown(self):

unittest.main(verbosity=2)


	#values not strings, ints, etc