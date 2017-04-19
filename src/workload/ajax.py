# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from .models import Index

def get_globe():
    return globals()

def dir_data(pk):
    index = Index.objects.get(pk=pk)
    index.childs.all()
    return{'stat':'sg'}

def dir_create(name,par=None):
    i = Index.objects.create(par_id=par,name=name)
    return {'status':'success','data':{'pk':i.pk,'name':i.name}}