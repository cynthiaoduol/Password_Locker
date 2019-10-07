import unittest 
from locker import User
from locker import Credentials

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Method to run before each user test cases.
        '''
        self.new_user = User("FeistyDory","21038")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,'FeistyDory')
        self.assertEqual(self.new_user.password,'210sda38')


    def test_save_user(self):
        '''
        test case to test if a new user object has been saved into the User list
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''

    def setUp(self):
        '''
        Method that runs before each credentials test case.
        '''
        self.new_credential = Credentials("Gmail","dorydory","143811jsa")

    


if __name__ == "__main__":
    unittest.main() 