#!/usr/bin/python3
""" The Orders Table"""
import tables
from tables.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime


class Order(BaseModel, Base):
    """Representation of Order"""
    __tablename__ = 'tOrder'
    id = Column(String(32), nullable=False, primary_key=True)
    OrderDate = Column(DateTime, default=datetime.utcnow)
    CustomerID = Column(String(32), ForeignKey('tCustomer.id'), nullable=False)
    Value = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)