from flask_cors import CORS
from config import api, app
from resources.FileManager import Upload,Delete
from resources.Register import Register
from resources.Login import Login
from resources.ListUserFiles import ListUserFiles
from resources.Profiling import Profiler

api.add_resource(Upload,'/uploadfile')
api.add_resource(Register,'/register')
api.add_resource(Login,'/login')
api.add_resource(ListUserFiles,'/getuserfiles')
api.add_resource(Delete,'/deleteuserfile')
api.add_resource(Profiler,'/profile')
CORS(app)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)