from _typeshed import Self
import json
from typing_extensions import Required

from django.http import request, response
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT ='wrest/'


# to  get records
def get_resources(id=None):
    data={}
    if id is not None:
        data={
            'id':id
        }
        resp =request.get(BASE_URL+ENDPOINT,data=json.dumps(data))
        print(resp.status_code)
        print(resp.json())
get_resources(1)


#to create member
def Create_resouces():
    new_std ={
        'name':'Dhoni',
        'rollno':105,
        'marks':32,
        'gf':'Disha',
        'bf':'Nora'
    }
    resp = request.post(BASE_URL+ENDPOINT,data=json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())
Create_resouces()

#to update member
def update_resouces(id):
    new_data={
        'id':id ,
        'name':'pradeep',
        'rollno': 1452
            }
    resp = request.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(resp.status_code)
    print(resp.json())
update_resouces(2)


#to delete member
def delete_resouces(id):
    data ={
        'id':id
        }
    r=request.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.status_code)
    print(r.json())
delete_resouces(2)
