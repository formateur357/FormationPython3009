import unittest

from exercices.Jour3.Exemples.tests.test_calcul import test_addition, test_division_par_zero
# from test_api import TestAPI

if __name__ == '__main__':
  loader = unittest.TestLoader()
  suite = unittest.TestSuite()

  suite.addTests(loader.loadTestsFromTestCase(test_addition))
  suite.addTests(loader.loadTestsFromTestCase(test_division_par_zero))
  # suite.addTests(loader.loadTestsFromModule(TestAPI))
  
  runner = unittest.TextTestRunner(verbosity=2)
  runner.run(suite)