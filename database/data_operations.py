#!/usr/bin/python3
""" 
module which has all functions of operations 
which can be applied to database 
"""
from sqlalchemy.orm import sessionmaker, Session
from email_table import engine, Email


Session = sessionmaker(bind=engine)
session = Session()


def insert_data(email="", ip=None):
    """ insert data into data base """

    e = Email(email_address = email, ip_address = ip)
    session.add(e)
    session.commit()

def close_session():
    """ remove the session """
    session.close()
