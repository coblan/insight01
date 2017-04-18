# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from django.contrib import admin
from .models import Work,WorkRecord
from helpers.director.shortcut import page_dc,FormPage,TablePage,ModelTable,ModelFields,model_dc

# Register your models here.

class WorkForm(ModelFields):
    class Meta:
        model=Work
        exclude=[]

class WorkFormPage(FormPage):
    fieldsCls=WorkForm

class WorkTable(ModelTable):
    model=Work

class WorkTablePage(TablePage):
    template='workload/work.html'
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
        
    


model_dc[Work]={'fields':WorkForm}
model_dc[WorkRecord]={'fields':WorkRecordForm}

page_dc.update({
    'work':WorkTablePage,
    'work.edit':WorkFormPage,
    'workrecord':WorkRecordTablePage,
    'workrecord.edit':WorkRecordFormPage,
})