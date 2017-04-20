# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from .models import Index
from helpers.director.db_tools import to_dict

def get_globe():
    return globals()

def dir_data(pk):
    index = Index.objects.get(pk=pk)
    index.childs.all()
    return{'stat':'sg'}

def dir_data(par):
    if par:
        query = Index.objects.filter(par_id=par)
    else:
        query = Index.objects.filter(par=None)
    rows=[to_dict(idx) for idx in query]
    
    parents=[]
    if par:
        this_dir=Index.objects.get(id=par)
        while this_dir.par:
            parents.append(this_dir.par)
            this_dir=this_dir.par
    parents.reverse()
    parents= [to_dict(idx) for idx in parents]
            
    return {'dirs':rows,'parents':parents}

def dir_create(name,par=None):
    if not par:
        i = Index.objects.create(name=name)
    else:
        i = Index.objects.create( par_id=par,name=name)
       
    return to_dict(i)