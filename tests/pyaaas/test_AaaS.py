import unittest

from pyaaas.aaas import AaaS


class AaaSTest(unittest.TestCase):

    def test_init(self):
        AaaS('http://localhost')
        
    def test_analyze(self):
        aaas= AaaS('http://localhost')
        aaas.analyze(dataset)


