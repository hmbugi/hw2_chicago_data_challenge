import unittest
from data_challenge import *

class TestFunctions(unittest.TestCase):
    def test_fileexist(self):
        '''Tests if all the dataset files exist'''
        self.assertTrue(fileexist('socio_eco_ind.csv'), True)
        self.assertTrue(fileexist('health_ind.csv'), True)
        self.assertTrue(fileexist('death_causes.csv'), True)

    def test_isreadable(self):
        self.assertTrue(isreadable('socio_eco_ind.csv'), True)
        self.assertTrue(isreadable('health_ind.csv'), True)
        self.assertTrue(isreadable('death_causes.csv'), True)

unittest.main()
