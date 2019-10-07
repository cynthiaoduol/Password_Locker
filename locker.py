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


