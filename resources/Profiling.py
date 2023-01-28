from flask_restful import Resource
from flask import request,jsonify,send_file
from AuthManager import require_auth
import os
from config import data_path
import pandas as pd
from pandas_profiling import ProfileReport
class Profiler(Resource):

    @require_auth
    def post(self,uid):
        print('generating report')
        df = pd.read_csv(os.path.join(data_path,*('99276faa-746f-4b00-b011-df1b3b2470c9','files','train (4).csv')))
        prof = ProfileReport(df, minimal=True,dark_mode=True)
        prof.to_file('rep.html')
        print('report generated. sending')
        return send_file(os.path.join(data_path,*('99276faa-746f-4b00-b011-df1b3b2470c9','files','rep.html')))
