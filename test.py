import unittest
from data_challenge import *

class TestFunctions(unittest.TestCase):
    def test_fileexist(self):
        '''Tests if all the dataset files exist'''
        self.assertTrue(fileexist('socio_eco_ind.csv'), True)
        self.assertTrue(fileexist('health_ind.csv'), True)
        self.assertTrue(fileexist('death_causes.csv'), True)

    def test_isreadable(self):
        '''Tests if all the dataset files are readable'''
        self.assertTrue(isreadable('socio_eco_ind.csv'), True)
        self.assertTrue(isreadable('health_ind.csv'), True)
        self.assertTrue(isreadable('death_causes.csv'), True)

    def test_parserreturn(self):
        '''Tests if the parsers return lists''' 
        self.assertTrue(type(socioparser()), [])
        self.assertTrue(type(birthparser()), [])
        self.assertTrue(type(deathparser()), [])

    def test_parserreturnlength(self):
        self.assertTrue(len(socioparser()), 77)
        self.assertTrue(len(birthparser()), 77)
        self.assertTrue(len(deathparser()), 77)

unittest.main()
