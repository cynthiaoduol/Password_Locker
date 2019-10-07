class User:
    '''
    Create User class that generates new instances of a user
    '''
    user_list = []

    def __init__(self,username, password):
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

    # @classmethod
    # def display_user(cls):
    #     return cls.user_list

    # def delete_user(self):
    #     '''
    #     delete_account method deletes a  saved account from the list
    #     '''
    #     User.user_list.remove(self)

class Credentials():
    '''
    Create credentials class to create new objects of credentials
    '''
    credentials_list = []

    def __init__(self,account,userName, password):
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


