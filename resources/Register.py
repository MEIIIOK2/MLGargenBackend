from flask import request, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash
from config import conn, data_path
import uuid
import os


class Register(Resource):
    def post(self):

        data = request.get_json()
        # print(data)
        pwd = generate_password_hash(data['password'], method='sha256')
        uid = uuid.uuid4()
        email = data.get('email')
        # name = data.get('name')
        # print(type(uid))
        try:
            cur = conn.cursor()

            cur.execute("SELECT count(*) FROM users where email=(%s);", (email,))
            resp = cur.fetchone()
            # print(resp)
            if resp[0] == 0:
                cur.execute("INSERT INTO users VALUES (%s,%s,%s);", (str(uid), email, str(pwd)))
                conn.commit()
            cur.close()
            userdata = os.path.join(data_path,str(uid))
            if not os.path.exists(userdata):
                os.mkdir(userdata)
                os.mkdir(os.path.join(userdata, 'models'))
                os.mkdir(os.path.join(userdata, 'files'))
            return 200
        except BaseException as e:
            print(e.args)
            conn.rollback()
