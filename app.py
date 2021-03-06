from flask import Flask
from flask import Response
from flask_restplus import Resource, Api
from flask_restplus import reqparse
import json
import dave


app = Flask(__name__)
api = Api(app, version='1.0', title='DAVE(Data Service)', description='Data Query REST API')

columnsns  = api.namespace('columnsquery', description='Data Columns')
datans  = api.namespace('dataquery', description='Data Query')


@columnsns.route('/<fname>', endpoint='columnsquery')
@columnsns.doc(params={'fname': 'File Name'})
class GetColumns(Resource):
    @columnsns.doc(responses={200: 'OK'})
    @columnsns.doc(responses={403: 'Forbidden'})
    @columnsns.doc(responses={500: 'Internal Server Error'})
    def get(self, fname):
        lst = dave.column_names(fname)

        return Response(json.dumps(lst),  mimetype='application/json')


@datans.route('/<fname>/<cname>', endpoint='dataquery')
@datans.doc(params={'fname': 'File Name', 'cname' : 'Column name'})
class GetData(Resource):
    @datans.doc(responses={200: 'OK'})
    @datans.doc(responses={403: 'Forbidden'})
    @datans.doc(responses={500: 'Internal Server Error'})
    def get(self, fname, cname):
        lst = dave.data_by_column(fname, cname)

        return Response(json.dumps(lst),  mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
