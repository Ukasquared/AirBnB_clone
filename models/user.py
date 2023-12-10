#!/usr/bin/env python3
""" importing the parent class """
from models.base_model import BaseModel


class User(BaseModel):
    """
    A class User that inherites from BseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
