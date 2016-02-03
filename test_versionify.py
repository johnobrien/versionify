'''
Created on Dec 14, 2015

@author: john.obrien
'''
import unittest
from versionify import versionify
import os
from freezegun import freeze_time


class Test(unittest.TestCase):

    def setUp(self):
        self.fp = os.path.abspath("test_file.txt")
        current_path, _ = os.path.split(self.fp)
        directory = os.path.join(current_path,  "Old Versions")
        self.new_fp = os.path.join(directory,
                              "test_file-John.OBrien-2012.01.14.12.00.01.txt")

    def tearDown(self):
        os.remove(self.new_fp)

    @freeze_time("2012-01-14 12:00:01")
    def testName(self):
        versionify(self.fp)
        self.assertTrue(os.path.exists(self.new_fp))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
