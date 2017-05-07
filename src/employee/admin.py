# encoding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from helpers.director.shortcut import FormPage,TablePage,ModelFields,ModelTable,page_dc,model_dc,permit_list,TabGroup
from helpers.director.db_tools import to_dict
from django.contrib import admin
from .models import EmployeeModel,BasicInfo
from django.contrib.auth.models import User
from django.db.models import Q
from helpers.common.employee import employee_admin
from helpers.common import human
# Register your models here.



#class BasicInfoFields(ModelFields):
    
    #class Meta:
        #model=BasicInfo
        #exclude=[]
    
    #def get_heads(self):
        #heads=super(BasicInfoFields,self).get_heads()
        #for head in heads:
            #if head.get('name')=='head':
                #head['type']='picture'
                #head['config']={
                #'crop':True,
                #'aspectRatio': 1,
                #'size':{'width':250,'height':250}
            #}
        #return heads

#class EmployeeFields(ModelFields):
    
    #class Meta:
        #model=EmployeeModel
        #exclude=[]
    
    #def dict_options(self):
        #options={}
        #users = list(User.objects.filter(employeemodel=None))
        #if self.instance.user:
            #users.append(self.instance.user)
        #options['user']=[{'value':user.pk,'label':unicode(user)}for user in users]
        #return options   
    
    #def get_options(self):
        #options= super(EmployeeFields,self).get_options()
        #users = list(User.objects.filter(employeemodel=None))
        #if self.instance.user:
            #users.append(self.instance.user)
        #options['user']=[{'value':user.pk,'label':unicode(user)}for user in users]
        #return options
    
    #def get_heads(self):
        #heads = super(EmployeeFields,self).get_heads()
        #for head in heads:
            #if head.get('name')=='user':
                #head['forign']=True
        #return heads
    

#class EmployeeFormPage(FormPage):
    #fieldsCls=EmployeeFields
    #template='director/fieldset.html'
    #def __init__(self, request):
        #self.request=request
        #self.pk=request.GET.get('pk')
        
        #if self.pk:
            #emp = EmployeeModel.objects.get(pk=self.pk)
        #else:
            #emp=EmployeeModel()
            
        #empf=EmployeeFields(instance=emp,crt_user=request.user)
        
        #baseinfo = emp.baseinfo or BasicInfo()
        #basf = BasicInfoFields(instance=baseinfo,crt_user=request.user)
        #self.ctx={
            #'fieldset':{
                #'employee':empf.get_context(),
                #'baseinfo':basf.get_context(),
            #},
            #'delset':['employee','baseinfo'],
            #'namelist':[{'label':'账户信息','fields':['employee.user']},
                        #{'label':'基本信息','fields':['baseinfo.name','baseinfo.age','baseinfo.head']}],
            #'save_step':[{'save':'baseinfo'},
                        #{'assign':'baseinfo','obj':'employee','value':'baseinfo'},
                        #{'save':'employee'},]
        #}
        
        
    

#class EmployeeTable(ModelTable):
    #model=EmployeeModel
    ##exclude=['baseinfo']
    
    #def dict_row(self, inst):
        #dc={
            #'user':unicode(inst.user),
            #'baseinfo':unicode(inst.baseinfo)
        #}
        #return dc
    # def get_rows(self):
        # """
        # """
        # query=self.get_query()
        # return [to_dict(x, include=self.permited_fields(),filt_attr=lambda row:{'user':unicode(row),'head':row.baseinfo.head}) for x in query]     

#class EmployeeTablePage(TablePage):
    #tableCls=EmployeeTable

#class EmployeeTablePageWX(EmployeeTablePage):
    #template='employee/m_emp_table.html'

#class EmployeeFormPageWX(EmployeeFormPage):
    #template='wx/fieldset.html'
 

emp_admin = employee_admin(BasicInfo, EmployeeModel)

model_dc[BasicInfo]={'fields': emp_admin['BasicInfoFields']}
model_dc[EmployeeModel]={'fields':emp_admin[ 'EmployeeFields']}

permit_list.append(EmployeeModel)
permit_list.append(BasicInfo)

page_dc.update(emp_admin['engine_dict'])

#page_dc.update({
    #'employee':EmployeeTablePage,
    #'employee.edit':EmployeeFormPage,
    #'employee.wx':EmployeeTablePageWX,
    #'employee.wx.edit':EmployeeFormPageWX,
#})


#page_dc.update({
    #'employee.edit':emp_admin['EmpGroup'],
#})