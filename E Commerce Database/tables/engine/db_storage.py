#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import tables
from tables.base_model import BaseModel, Base
from tables.product import Product
from tables.customer import Customer
from tables.order import Order
from tables.order_detail import OrderDetail
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

classes = {"Product": Product, "Customer": Customer,
           "Order": Order, "OrderDetail": OrderDetail}
load_dotenv()


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        ECOM_MYSQL_USER = getenv('ECOM_MYSQL_USER')
        ECOM_MYSQL_PWD = getenv('ECOM_MYSQL_PWD')
        ECOM_MYSQL_HOST = getenv('ECOM_MYSQL_HOST')
        ECOM_MYSQL_DB = getenv('ECOM_MYSQL_DB')
        try:
            self.__engine = create_engine('mysql+mysqlconnector://{}:{}@{}/{}'.
                                          format(ECOM_MYSQL_USER,
                                                 ECOM_MYSQL_PWD,
                                                 ECOM_MYSQL_HOST,
                                                 ECOM_MYSQL_DB))
        except sqlalchemy.exc.SQLAlchemyError as e:
            print(f"Error connecting to the database: {e}")
    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = tables.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(tables.storage.all(clas).values())
        else:
            count = len(tables.storage.all(cls).values())

        return count