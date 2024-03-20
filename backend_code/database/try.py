#!/usr/bin/python3

from data_operations import insert_data, close_session, get_data_with_email, get_data
from sqlalchemy.exc import SQLAlchemyError

try:
    insert_data("ahmed@gmail.com")
    email = get_data_with_email("MO@gmail.com")
    data = get_data()
    print(email)
    print(data)
    close_session()

except SQLAlchemyError as e:
    print("An error occurred while handling the database operation.")
    print(str(e))
