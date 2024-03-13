#!/usr/bin/python3

from data_operations import insert_data, close_session
from sqlalchemy.exc import SQLAlchemyError

try:
    insert_data("mo@gmail.com", "126.134.5.5")
    close_session()
except SQLAlchemyError as e:
    print("An error occurred while handling the database operation.")
    print(str(e))
