#!/usr/bin/env python3
""" model to instance ond subclass"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """ initializes the instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def __str__(self):
        """returs information about the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the time when object is modified"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """ creates a dictionary of instance"""
        self.created_at.isoformat()
        self.updated_at.isoformat()
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict