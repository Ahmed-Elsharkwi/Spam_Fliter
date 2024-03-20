#!/usr/bin/python3
""" module of email table """


import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.orm import declarative_base
from datetime import datetime


engine = create_engine("mysql://root:Ahmede2*@localhost/hbnb_dev_db", pool_size=10, max_overflow=20)
Base = declarative_base()


class Email(Base):
    """ initialise the email table """
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(1000), nullable=False)
    ip_address = Column(String(1000))
    created_on = Column(DateTime(), default=datetime.now)

Base.metadata.create_all(engine)
