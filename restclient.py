from requests import put, get
import json
#lis=put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
import db

val1=10
val2=20

#
# lis=put('http://localhost:5000/todo1', data={'data':val1, 'data1':val2}).json()
# print("This is put result from server is : ",lis)



def pinging(sel):
    pingdata=db.pingdata(sel)
    print(pingdata)
    data_json=json.dumps(pingdata)
    res=get('http://localhost:5000/'+data_json).json()
    print("This is get request in the result comming from server: ",res)
    return res

def startup(sel):
    pingdata=db.pingdata(sel)
    print(pingdata)
    data_json=json.dumps(pingdata)
    res=get('http://localhost:5000/restdata/'+data_json).json()
    print("This is get request in the result comming from server: ",res)
    return res

# put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
#
# get('http://localhost:5000/todo2').json()


