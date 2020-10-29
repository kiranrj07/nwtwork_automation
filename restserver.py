from flask import Flask, request
from flask_restful import Resource, Api
import json
import pingg
import start1

app = Flask(__name__)
api = Api(app)

# class Execute_cmd(Resource):
#     def put(self, cmd):
#         print("I am printing anyval here", cmd)
#         fulval = request.form['data']
#
#         fulval1 = request.form['data1']
#         print("I am printing fulval here: ",fulval)
#         print("I am printing fulval1 here: ", fulval1)
#         result=fulval+fulval1
#         print("I am printing restult at server : ",result)
#         return result


class Pinging(Resource):
    def get(self,ping_data):
        print("simp is: ", ping_data)
        jdata=json.loads(ping_data)

        print(type(jdata))
        print('I am printing ip address here: ',jdata['device']['ip_addr'])

        result=pingg.ping(jdata['device']['ip_addr'])
        #print("result from ping is: ",result)
        return {'result': result}, 201, {'Etag': 'some-opaque-string'}


class starting(Resource):
    def get(self,start_data):


        #print("I have successfull entered into staring block and printing start data as: ",start_data)
        result=start1.wake(start_data)
        return {'result': result}, 201, {'Etag': 'some-opaque-string'}

#api.add_resource(Execute_cmd, '/<string:cmd>')

api.add_resource(Pinging, '/<string:ping_data>')
api.add_resource(starting, '/restdata/<string:start_data>')

if __name__ == '__main__':
    app.run(debug=True)