# Password_Locker

#### Author: [cynthiaoduol](https://github.com/cynthiaoduol)

## Description

This project is a python application that manages login and signup credentials of a person for various accounts i.e. username and passwords for each account. It also stores the passwords and generates a unique password for a user if they do not want to generate new passwords by themselves.


## User Stories
The user would like to.... :
* Create an account for the application or log into the application.
* Store my existing acounts login details for various accounts that i have registered for.
* Generate new password for an account that i haven't registered for and store it with the account name.   
* Delete stored account login details that i do now want anymore.
* Copy my credentials to clipboard.

## Installation / Setup instruction

**These Simple Instructions will get you a copy of the application running on your terminal.**

1. Get into the **Project Repository.**

Link:-> ```https://github.com/cynthiaoduol/Password_Locker)```

2. Clone the project.

3. Get into project folder (cd into project).

4. If you have all the Pre-requisites you can run the application.

### Pre-requisites

**What things you need to install the application and how to install them.**

```
Python3.6
```

To Install **python 3.6** on terminal execute

```
apt-get install python3.6
```

```
apt-get install pip3
```

## Running the application

1. Navigate into the cloned folder using terminal and enter command `./password.py` to run the app.
The app will open on terminal 

2. Follow and answer the prompts to use the application.

## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./password.py```|Hello Welcome to your Password Store... <br>* CA ---  Create New Account * HA ---  Have An Account |
|Select  CA| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select HA  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```tp``` to enter your password or ```gp``` for the application to generate a password for you |
|Display all stored credentials | Enter ```DC```|A list of all credentials that has been stored or ```You don't have any credentials saved yet``` |
|Find a stored credential based on account name|Enter ```FC```| Enter the Account Name you want to search for and returns the account details|
|Delete an existing credential that you don't want anymore|Enter ```D```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exist|
|Exit the application| Enter ```D```| The application exits|

## Built With

* [Python3.6](https://docs.python.org/3/)

## Support and contact details
 Incase you come across errors, have questions, ideas ,concerns, or want to contribute to the application, feel free to reach me at :cynthiaobu940@gmail.com

### License
*MIT licence*
Copyright (c) 2019 **Cynthia Oduol**


