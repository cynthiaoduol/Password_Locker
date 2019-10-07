import random
import string


class User:
    '''
    Create User class that generates new instances of a user
    '''
    user_list = []

    def __init__(self, username, password):
        '''
        method that defines the properties for user objects 
        '''
        self.username = username
        self.password = password

    def save_user(self):
        '''
        A method that saves a new user instace into the user list
        '''
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        method that deletes a saved account from the list
        '''
        User.user_list.remove(self)


class Credentials():
    '''
    Create credentials class to create new objects of credentials
    '''
    credentials_list = []

    def __init__(self, account, userName, password):
        '''
        method that defines user credentials to be stored
        '''
        self.account = account
        self.userName = userName
        self.password = password

    def save_details(self):
        '''
        method to save a new credential instance to the credentials list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method that deletes an account credentials from the credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_credential(cls, account):
        '''
        Method that takes in a account_name and returns a credential that matches that account_name.

        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential

    @classmethod
    def if_credential_exist(cls, account):
        '''
        Method that checks if a credential exists from the credential list and returns true or false depending on whether the credential exists.
        '''
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        Method that returns all items in the credentials list
        '''
        return cls.credentials_list 


    def generatePassword(stringLength=8):
        '''
        Generate a random password string of letters and digits and special characters
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength)) 
