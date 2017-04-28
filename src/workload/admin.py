# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib import admin
from .models import Work,WorkRecord,Index
from helpers.director.shortcut import page_dc,FormPage,TablePage,ModelTable,ModelFields,model_dc,RowFilter,permit_list


# Register your models here.
class IndexForm(ModelFields):
    class Meta:
        model=Index
        fields=['name']

class WorkForm(ModelFields):
    class Meta:
        model=Work
        exclude=['index']

class WorkFormPage(FormPage):
    fieldsCls=WorkForm

class WorkTable(ModelTable):
    model=Work

class WorkTablePage(TablePage):
    tableCls=WorkTable


class WorkRecordForm(ModelFields):
    class Meta:
        model=WorkRecord
        exclude=[]
    
class WorkRecordFormPage(FormPage):
    fieldsCls=WorkRecordForm


class WorkRecordFilter(RowFilter):
    names=['status']
    range_fields=[{'name':'create_time','type':'date'}]
    model=WorkRecord 

class WorkRecordTable(ModelTable):
    model=WorkRecord
    filters=WorkRecordFilter
    
    def inn_filter(self, query):
        query =super(WorkRecordTable,self).inn_filter(query)
        return query.order_by('-id')

class WorkRecordTablePage(TablePage):
    tableCls=WorkRecordTable

class WorkRecordFormPageWX(WorkRecordFormPage):
    template='workload/m_workrecord_form.html'

class WRselfForm(ModelFields):
    readonly=['emp','status']
    class Meta:
        model=WorkRecord
        exclude=[]
    
    def get_row(self):
        
        if not self.instance.pk:
            self.instance.emp= self.crt_user.employeemodel_set.first()
            self.instance.save()
        return super(WRselfForm,self).get_row()
        
class WRselfFormPage(FormPage):
    template='workload/m_workrecord_form.html'
    fieldsCls=WRselfForm
    
class WRselfTable(ModelTable):
    model=WorkRecord
    filters=WorkRecordFilter
    def inn_filter(self, query):
        query =super(WRselfTable,self).inn_filter(query)
        return query.filter(emp__user=self.crt_user).order_by('-id')

class WRselfTablePage(TablePage):
    tableCls=WRselfTable


        
class WorkIndex(FormPage):
    template='workload/work.html'
    def __init__(self,request):
        self.request=request
        self.ctx={
            'app':'workload',
            'heads':WorkForm(crt_user=self.request.user).get_heads(),
            'dir_heads':IndexForm(crt_user=self.request.user).get_heads(),
        }
        
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
    'workrecord.wx':WorkRecordTablePage,
    
    'workrecord.edit':WorkRecordFormPage,
    'workrecord.wx.edit':WorkRecordFormPageWX,
    
    'wkself.wx':WRselfTablePage,
    'wkself.wx.edit':WRselfFormPage,
})