# config.py
import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="istroman21",
        password="-",
        hostname="istroman21.mysql.eu.pythonanywhere-services.com",
        databasename="istroman21$basketDB"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
