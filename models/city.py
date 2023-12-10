#!/usr/bin/env python3
"""
importing the parent class from BaseModel
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    will contain information about the states
    """
    state_id = ""
    name = ""
