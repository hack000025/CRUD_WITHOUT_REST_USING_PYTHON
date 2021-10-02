import json
from django.core.serializers import register_serializer
from django.shortcuts import render, render_to_response
from django.views.generic import View
from wrestm.utils import  is_json
from wrestm.mixin import HttResponseMixin ,SerializeMixin
from wrestm.models import Student
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from wrestm.forms import StudentForm


@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDCBV(HttResponseMixin, View):
    def get(self,request,*args,**kwargs):
        def get_object_by_id(self,id):
            try:
                s = Student.objects.get(id=id)
            except Student.DoesNotExist:
                s=None
            return s 

        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'plz provide valide json data only'}),status=400)
            p_data = json.loads(data)
            if id is not None:
                std = self.get_object_by_id(id)
                if std in  None :
                    return self.render_to_http_response(json.dumps({'msg':'no record found with matched id '}),status=400)
            json_data=self.serialize([std,])
            return self.render_to_http_response(json_data)
        if id is None:
            qs = Student.objects.all()            
            json_data = self.serialize(qs)
            return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data =request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response({'msg':'plz provide valid json data'},status=400)
        std_data = json.load(data)
        form = StudentForm(std_data)
        if form.is_valid():
            form.save(commit=True)        
            return self.render_to_http_response(json.dumps({'msg':'record inserted succucessfully'}))
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json =json.dumps(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'plz provide valid data'}),status=400)
        p_data = json.loads(data)
        id = request.get('id',None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'plz provide id for updation'}),status=400)
        std = self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'no matched record found with provided id'}),status=400)
        orginal_data={
            'name':std.name,
            'rollno':std.rollno,
            'marks':std.marks,
            'gf':std.gf,
            'bf':std.bf
        }
        orginal_data.update(p_data)
        form = StudentForm(orginal_data,instance=std)
        if form.is_valid():
            form.save(commit=True)
            return self.render_to_http_response(json.dumps({'msg':'record updated succussfully'}))

        if form.errors():
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json =is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'plz providfe valid data'}),status=400)
        p_data = json.loads(data)
        id = p_data.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'plz provide id to delete'}),status=400)
        std =self.request.get('id',None)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'provided id is not matched with records'}),status=400)
        status,deleted_item = std.delete()
        if status == 1 :
            json_data = json.dumps({'msg':'record deleted successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps(json.dumps({'msg':'unable to delete plz try again.............'}),status=500)








