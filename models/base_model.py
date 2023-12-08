#!/usr/bin/env python3
""" model to instance ond subclass"""
import uuid
from datetime import datetime
import models

class BaseModel:
<<<<<<< HEAD
    """create the base class"""
    def __init__(self):
        """ initializes the instance"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)
=======
    def __init__(self, *args, **kwargs):
        """ initializes the instance"""
        if kwargs:
            # if kwargs is not empty, we reconstruct from s dic
            for key, value in kwargs.items():
                # if key is class, skip
                if key == '__class__':
                    continue
                # then we set the attribute to self
                setattr(self, key, value)
                if key in ['created_at', 'updated_at']:
                    # make datetime string to datetime object
                    setattr(self, key, datetime.now())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
    
>>>>>>> ef5cc43e66bd67cbdbf7442afd7e7a25edfeeb1d
    def __str__(self):
        """returns information about the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the time when object is modified"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ creates a dictionary of instance"""
<<<<<<< HEAD
=======
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
>>>>>>> ef5cc43e66bd67cbdbf7442afd7e7a25edfeeb1d
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
