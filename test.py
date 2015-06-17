from unittest import *
from data_challenge import *

class TestFunctions(unittest.TestCase):
    def test_fileexist(self):
        '''Tests if all the dataset files exist'''
        self.assertTrue(fileexist('socio_eco_ind.csv'), True)
        self.assertTrue(fileexist('health_ind.csv'), True)
        self.assertTrue(fileexist('death_causes.csv'), True)
