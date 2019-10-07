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
        self.new_user = User("FeistyDory","210sda38")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"FeistyDory")
        self.assertEqual(self.new_user.password,"210sda38")


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


    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []


    def test_init(self):
        '''
        Test case to check if a new Credentials instance has been initialized correctly
        '''
        self.assertEqual(self.new_credential.account,"Gmail")
        self.assertEqual(self.new_credential.userName,"dorydory")
        self.assertEqual(self.new_credential.password,"143811jsa") 


    def save_credential_test(self):
        '''
        test case to test if the credential object is saved into the credentials list.
        '''
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("instagram","feistydory","qwerty") 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("instagram","feistydory","qwerty") 
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)


    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("instagram","feistydory","qwerty") 
        test_credential.save_details()

        the_credential = Credentials.find_credential("instagram")

        self.assertEqual(the_credential.account,test_credential.account)


    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_details()
        the_credential = Credentials("instagram","feistydory","qwerty") 
        the_credential.save_details()
        credential_is_found = Credentials.if_credential_exist("instagram")
        self.assertTrue(credential_is_found)


    def test_display_all_saved_credentials(self):
        '''
        test case to check if method that displays all the credentials that has been saved by the user
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)


if __name__ == "__main__":
    unittest.main() 