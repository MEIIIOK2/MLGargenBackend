import flask
from flask import Flask , jsonify, request
from flask_restful import Resource, Api

from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
import pandas as pd
import json

from utils import Config
import time
import numpy as np
import os
import uuid
import psycopg2
import jwt
import datetime
from glob import glob
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED


app = Flask(__name__)

api = Api(app)
config = Config()
app.config['SECRET_KEY']=config.secret
a = time.time()
data_path = config.datapath_test
conn = psycopg2.connect(
            host=config.host,
            database=config.database,
            user=config.user,
            password=config.password)
