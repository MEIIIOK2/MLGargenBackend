from flask_restful import Resource
from flask import request,jsonify
from AuthManager import require_auth
import os
from config import data_path

class ListUserFiles(Resource):
    @require_auth
    def get(self, uid=None):
        files_path = os.path.join(data_path,*(uid,'files'))
        files = os.listdir(files_path)
        print(files)
        response = []
        for file in files:
            response.append({'filename':file,'size':os.path.getsize(os.path.join(files_path,file))})
        print(response)
        return jsonify(response)