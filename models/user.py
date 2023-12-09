#!/usr/bin/env python3
""" importing the parent class """
from base_model import BaseModel

class User(BaseModel):
    """
    A class User that inherites from BaseModel
    """
    def __init__(self, email, password, first_name, last_name):
        """
        initialization of the class
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
