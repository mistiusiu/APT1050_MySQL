#!/usr/bin/python3
""" The OrderDetail Table"""
import tables
from tables.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from datetime import datetime


class OrderDetail(BaseModel, Base):
    """Representation of OrderDetail"""
    __tablename__ = 'tOrderDetail'
    id = Column(String(32), nullable=False, primary_key=True)
    SalesOrderID = Column(String(32), ForeignKey('tOrder.id'), nullable=False)
    ProductID = Column(String(32), ForeignKey('tProduct.id'), nullable=False)
    OrderQty = Column(Integer, nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the class"""
        super().__init__(*args, **kwargs)