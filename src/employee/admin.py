# encoding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from helpers.director.shortcut import FormPage,TablePage,ModelFields,ModelTable,page_dc,model_dc,permit_list

from django.contrib import admin
from .models import EmployeeModel,BasicInfo

# Register your models here.



class BasicInfoFields(ModelFields):
    
    class Meta:
        model=BasicInfo
        exclude=[]

class EmployeeFields(ModelFields):
    
    class Meta:
        model=EmployeeModel
        exclude=[]

class EmployeeFormPage(FormPage):
    fieldsCls=EmployeeFields
    template='director/fieldset.html'
    def __init__(self, request):
        self.request=request
        self.pk=request.GET.get('pk')
        
        if self.pk:
            emp = EmployeeModel.objects.get(pk=self.pk)
        else:
            emp=EmployeeModel()
            
        empf=EmployeeFields(instance=emp,crt_user=request.user)
        
        baseinfo = emp.baseinfo or BasicInfo()
        basf = BasicInfoFields(instance=baseinfo,crt_user=request.user)
        self.ctx={
            'fieldset':{
                'employee':empf.get_context(),
                'baseinfo':basf.get_context(),
            },
            'delset':['employee','baseinfo'],
            'namelist':[{'label':'账户信息','fields':['employee.user']},
                        {'label':'基本信息','fields':['baseinfo.name','baseinfo.age']}],
            'save_step':[{'save':'baseinfo'},
                        {'assign':'baseinfo','obj':'employee','value':'baseinfo'},
                        {'save':'employee'},]
        }
        
        
    

class EmployeeTable(ModelTable):
    model=EmployeeModel

class EmployeeTablePage(TablePage):
    tableCls=EmployeeTable
 
model_dc[BasicInfo]={'fields':BasicInfoFields}
model_dc[EmployeeModel]={'fields':EmployeeFields}

permit_list.append(EmployeeModel)
permit_list.append(BasicInfo)

page_dc.update({
    'employee':EmployeeTablePage,
    'employee.edit':EmployeeFormPage
})