from flask_restful import Resource
from flask import request
from AuthManager import require_auth
import os
from config import data_path
class Upload(Resource):
    @require_auth
    def post(self,uid = False):
        file = request.files.getlist('file')[0]
        filename = file.filename
        # print(filename)
        user_files_path = os.path.join(data_path,*(uid,'files'))
        file.save(os.path.join(user_files_path,filename))
        return {'ok':'ok'}