from flask_restful import Resource
from flask import request, jsonify
from AuthManager import require_auth
import os
from config import data_path

class Upload(Resource):
    @require_auth
    def post(self,uid = False):
        file = request.files.getlist('file')[0]
        filename = file.filename
        # print(file)
        user_files_path = os.path.join(data_path,*(uid,'files'))
        file.save(os.path.join(user_files_path,filename))
        return {'ok':'ok'}


class Delete(Resource):
    @require_auth
    def post(self,uid = False):
        filename = request.get_json().get('filename')
        print(filename)
        user_files_path = os.path.join(data_path,*(uid,'files'))
        os.remove(os.path.join(user_files_path,filename))
        return {'ok':'ok'}