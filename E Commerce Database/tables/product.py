#!/usr/bin/python3
""" The Products Table"""
import tables
from tables.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """Representation of Product """
    __tablename__ = 'tProduct'
    id = Column(String(32), nullable=False, primary_key=True)
    ProductName = Column(String(256), nullable=False)
    Colour = Column(String(32), nullable=False)
    ReorderPoint = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)