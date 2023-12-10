#!/usr/bin/env python3
""" importing the class """
from models.base_model import BaseModel

class Review(BaseModel):
    """
    inherit from basemodel
    """
    # createing a public class attributes
    # All has to be empty
    place_id = ""
    user_id = ""
    text = ""

