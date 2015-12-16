'''
Created on Dec 14, 2015

@author: john.obrien
'''
import unittest
from versionify import versionify

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass
        # Need to delete the backup created by this test...

    def testName(self):
        versionify("test_file.txt")
        # How do I test for the existence of the backup file here?


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()