from flask_cors import CORS
from config import api, app
from resources.Upload import Upload
from resources.Register import Register
from resources.Login import Login
from resources.ListUserFiles import ListUserFiles

api.add_resource(Upload,'/uploadfile')
api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(ListUserFiles,'/getuserfiles')
CORS(app)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)