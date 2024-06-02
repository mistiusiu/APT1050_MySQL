#!/usr/bin/python3
""" The Customers Table"""
import tables
from tables.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Customer(BaseModel, Base):
    """Representation of Customer """
    __tablename__ = 'tCustomer'
    id = Column(String(32), nullable=False, primary_key=True)
    FirstName = Column(String(64), nullable=False)
    LastName = Column(String(64), nullable=False)
    EmailAddress = Column(String(64), nullable=False)
    AddressLine1 = Column(String(128), nullable=False)
    City = Column(String(64), nullable=False)
    PostalCode = Column(String(16), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)