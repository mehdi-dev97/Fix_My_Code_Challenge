#!/usr/bin/python3
""" 
User module class
"""

class User():
    """ User class """
    
    def __init__(self):
        """ Initialize the user """
        self.__email = None

    @property
    def email(self):
        """ get email value """
        return self.__email

    @email.setter
    def email(self, value):
        """ Set new value in email """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value
   
    
if __name__ == "__main__":
    """ New instance of user """
    u = User()
    u.email = "john@snow.com"
    print(u.email)