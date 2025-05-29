import os
from dotenv import load_dotenv

class ConfigDB:
    HOST = os.getenv('HOST')
    USER = os.getenv('USER')
    PASSWORD = os.getenv('DBPASSWORD')
    PORT = os.getenv('PORT')
    NAME = os.getenv('DBNAME')