import os
from dotenv import load_dotenv
import base64
class Config:
    load_dotenv()
    host = os.environ.get('HOST')
    database = os.environ.get('DATABASE')
    user = os.environ.get('DBUSER')
    password = os.environ.get('PASSWORD')
    secret = os.environ.get('SECRET')
    datapath_prod = os.environ.get('DATAPATH_PROD')
    datapath_test = os.environ.get('DATAPATH_TEST')