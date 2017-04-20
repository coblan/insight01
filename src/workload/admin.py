# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib import admin
from .models import Work,WorkRecord,Index
from helpers.director.shortcut import page_dc,FormPage,TablePage,ModelTable,ModelFields,model_dc


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

class WorkRecordTable(ModelTable):
    model=WorkRecord

class WorkRecordTablePage(TablePage):
    tableCls=WorkRecordTable


#class WorkPage(object):
    #template='workload/work.html'
    #def __init__(self,request):
        #self.request=request
    
    #def get_context(self):
        #pass
        
class WorkIndex(FormPage):
    template='workload/work.html'
    def __init__(self,request):
        self.request=request
        self.ctx={
            'app':'workload',
            'heads':WorkForm(crt_user=self.request.user).get_heads(),
            'dir_heads':IndexForm(crt_user=self.request.user).get_heads(),
        }
    


model_dc[Work]={'fields':WorkForm}
model_dc[WorkRecord]={'fields':WorkRecordForm}
model_dc[Index]={'fields':IndexForm}

page_dc.update({
    'workindex':WorkIndex,
    'work':WorkTablePage,
    'work.edit':WorkFormPage,
    'workrecord':WorkRecordTablePage,
    'workrecord.edit':WorkRecordFormPage,
})