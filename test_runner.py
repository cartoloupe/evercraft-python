import unittest

suite = unittest.TestLoader().discover('tests', 'test_*.py')
unittest.TextTestRunner(verbosity=2).run(suite)
