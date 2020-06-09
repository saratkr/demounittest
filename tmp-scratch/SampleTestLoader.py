import unittest


# import your test modules
from .SampleFixturesTests import SimpleCalcFixturesTest

from . import SampleSimpleCalculTests

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add mytests to the test suite
suite.addTests(loader.loadTestsFromModule(SampleSimpleCalculTests))
suite.addTests(loader.loadTestsFromTestCase(SimpleCalcFixturesTest))
#suite.addTests(loader.loadTestsFromModule(scenario))
#suite.addTests(loader.loadTestsFromModule(thing))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)