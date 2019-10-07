import unittest 
from locker import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Method to run before each test cases.
        '''
        self.new_user = User("FeistyDory","21038")

    