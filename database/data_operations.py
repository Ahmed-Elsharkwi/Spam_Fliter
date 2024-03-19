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

def get_data_with_email(email=""):
    """ get the data of a specific email """
    try:
        data = session.query(Email).filter(Email.email_address == email).all()
        data_email = None
        for item in data:
            data_email = item.email_address
    except SQLAlchemyError as e:
        data_email = None
    return data_email


def get_data():
    """ get the whole data """
    data_dict = {"email_address": [], "ip": [], "created_date": []}
    try:
        data = session.query(Email).all()
        for item in data:
            data_dict["email_address"].append(item.email_address)
            data_dict["ip"].append(item.ip_address)
            data_dict["created_date"].append(item.created_on)
    except SQLAlchemyError as e:
        data_dict = None
    return data_dict

def close_session():
    """ remove the session """
    session.close()
