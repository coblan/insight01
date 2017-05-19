# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib import admin
from .models import Work,WorkRecord,Index
from helpers.director.shortcut import page_dc,FormPage,\
     TablePage,ModelTable,ModelFields,model_dc,RowFilter,permit_list,has_permit,ModelPermit
from django import forms

# Register your models here.
class IndexForm(ModelFields):
    class Meta:
        model=Index
        fields=['name']

class WorkForm(ModelFields):
    class Meta:
        model=Work
        exclude=['par']
    def get_heads(self):
        heads= super(WorkForm,self).get_heads()
        for head in heads:
            if head.get('name')=='desp_img':
                head['type']='picture'
                head['config']={
                'crop':True,
                'aspectRatio': 1,
                'size':{'width':250,'height':250}
            }
        return heads

class WorkFormPage(FormPage):
    fieldsCls=WorkForm

class WorkTable(ModelTable):
    model=Work
    def dict_row(self, inst):
        rt_dc={}
        if inst.desp_img:
            rt_dc['desp_img']='<img src="%s" width="30"/>'%inst.desp_img
        if inst.par:
            rt_dc['par']=unicode(inst.par)
        return rt_dc

class WorkTablePage(TablePage):
    tableCls=WorkTable


class WorkRecordForm(ModelFields):
    class Meta:
        model=WorkRecord
        exclude=[]
    
    def get_heads(self):
        heads= super(WorkRecordForm,self).get_heads()
        for head in heads:
            if head.get('name')=='desp_img':
                head['type']='picture'
                head['config']={
                'crop':True,
                'aspectRatio': 1,
                'size':{'width':250,'height':250}
            }
            elif head['name']=='finish_time':
                head['type']='date'            
        return heads  
    
    def clean(self):
        cleaned_data = super(WorkRecordForm,self).clean()
        if not has_permit(self.crt_user,'workrecord.check_all'):
            if self.instance.status!='waiting': 
                raise forms.ValidationError('you have no permition to edit this workrecord again')

    #def can_access(self):
        #access = super(WorkRecordForm,self).can_access()
        #if not has_permit(self.crt_user,'workrecord.check_all'):
            #if self.instance.status!='waiting':
                
    #def clean(self,*args,**kw):
        #cleaned_data = super(WorkRecordForm, self).clean()
        #if not cleaned_data.get('tmp') and not cleaned_data.get('work'):
            #self.add_error('work', '当非临时工作时，必须选择工时种类')
         
        
    
class WorkRecordFormPage(FormPage):
    fieldsCls=WorkRecordForm


class WorkRecordFilter(RowFilter):
    names=['status','work','ex_span']
    range_fields=[{'name':'create_time','type':'date'}]
    model=WorkRecord 

class WorkRecordTable(ModelTable):
    model=WorkRecord
    filters=WorkRecordFilter
    
    def inn_filter(self, query):
        query =super(WorkRecordTable,self).inn_filter(query)
        return query.order_by('-id')
    
    def dict_row(self,inst):
        dc={}
        if  inst.work:
            dc.update({
                'work_desp_img': inst.work.desp_img,
                'work':unicode(inst.work),
            })
        dc.update({
            'emp':unicode(inst.emp),
            'desp_img':inst.desp_img,            
        })
        return dc

class WorkRecordTablePage(TablePage):
    tableCls=WorkRecordTable
    
    def get_label(self):
        return '工作审批列表'

class WorkRecordTablePageWX(WorkRecordTablePage):
    template='workload/m_workrecord.html'

    #template='workload/m_workrecord.html'

class WorkRecordFormPageWX(WorkRecordFormPage):
    template='workload/m_workrecord_form.html'

class WRselfForm(ModelFields):
    readonly=['emp','status']
    class Meta:
        model=WorkRecord
        exclude=[]
    
    def get_row(self):
       
        #if not self.instance.pk:
        # 员工创建新workrecord时，自动添加上
        self.instance.emp= self.crt_user.employeemodel_set.first()
            #self.instance.save()
        return super(WRselfForm,self).get_row()
    
    def get_heads(self):
        heads= super(WRselfForm,self).get_heads()
        for head in heads:
            if head.get('name')=='desp_img':
                head['type']='picture'
                head['config']={
                'crop':True,
                'aspectRatio': 1,
                'size':{'width':250,'height':250}
            }
            elif head['name']=='finish_time':
                head['type']='date'
        if self.instance.status =='pass':
            for head in heads:
                head['readonly']=True
                
        return heads 
    
        
class WRselfFormPage(FormPage):
    template='workload/m_workrecord_form.html'
    fieldsCls=WRselfForm
    
class WRselfTable(ModelTable):
    model=WorkRecord
    filters=WorkRecordFilter
    def inn_filter(self, query):
        query =super(WRselfTable,self).inn_filter(query)
        return query.filter(emp__user=self.crt_user).order_by('-id')
    def dict_row(self, inst):
        return {
            'work': unicode(inst.work),
            'work_desp_img':inst.work.desp_img
        }

class WRselfTablePage(TablePage):
    tableCls=WRselfTable
    template='workload/m_workself.html'
    def get_label(self):
        emp=self.request.user.employeemodel_set.first()
        return '%s的工作提交记录'%emp.baseinfo.name


        
class WorkIndex(object):
    template='workload/work.html'
    def __init__(self,request):
        self.request=request
        
    def get_context(self):
        workform = WorkForm(crt_user=self.request.user)
        indexform=IndexForm(crt_user=self.request.user)
        self.ctx={
            'app':'workload',
            'heads':workform.get_heads(),
            'work_editable':bool( workform.permit.changeable_fields()),
            'work_can_add':workform.permit.can_add(),
            'dir_heads':indexform.get_heads(),
            'dir_editable':bool(indexform.permit.changeable_fields()),
            'dir_can_add':indexform.permit.can_add(),
        }
        return self.ctx
     
        
class WorkIndexWX(WorkIndex):
    template='workload/m_work.html'

permit_list.append(WorkRecord)
permit_list.append(Work)
permit_list.append({'name':'workrecord','label':'工作SP','fields':[
    {'name':'check_all','label':'查看所有工作','type':'bool'},
]})


model_dc[Work]={'fields':WorkForm}
model_dc[WorkRecord]={'fields':WorkRecordForm}
model_dc[Index]={'fields':IndexForm}

page_dc.update({
    'workindex':WorkIndex,
    'workindex.wx':WorkIndexWX,
    
    'work':WorkTablePage,
    'work.wx':WorkTablePage,
    
    'work.edit':WorkFormPage,
    'work.wx.edit':WorkFormPage,
    
    'workrecord':WorkRecordTablePage,
    'workrecord.wx':WorkRecordTablePageWX,
    
    'workrecord.edit':WorkRecordFormPage,
    'workrecord.wx.edit':WorkRecordFormPageWX,
    
    'wkself.wx':WRselfTablePage,
    'wkself.wx.edit':WRselfFormPage,
})