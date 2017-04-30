# encoding:utf-8

from __future__ import unicode_literals
from __future__ import absolute_import
from .models import Index,Work
from helpers.director.db_tools import to_dict,from_dict
from helpers.director.shortcut import ModelPermit
from django.core.exceptions import PermissionDenied

def get_global():
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
        parents.append(this_dir)
        while this_dir.par:
            parents.append(this_dir.par)
            this_dir=this_dir.par
    parents.reverse()
    parents= [to_dict(idx) for idx in parents]
    
    items=[]
    if par:
        this_dir=Index.objects.get(id=par)
        items=[to_dict(item) for item in this_dir.work_set.all()]
    else:
        items=[to_dict(item) for item in Work.objects.filter(index=None)]
    return {'dirs':rows,'parents':parents,'items':items}

def dir_create(user,par=None):
    if not ModelPermit(Index,user).can_add():
        raise PermissionDenied,'not permit create index'
    if not par:
        i = Index.objects.create()
    else:
        i = Index.objects.create( par_id=par)
       
    return to_dict(i)

def item_create(par):
    par=par or None
    work = Work.objects.create(index_id=par)
    return to_dict(work)

def items_paste(rows,par):
    if par:
        par_index=Index.objects.get(pk=par)
    else:
        par_index=None
    for row in rows:
        inst = from_dict(row)
        if isinstance(inst,Index):
            inst.par=par_index
        elif isinstance(inst,Work):
            inst.index=par_index
        inst.save()
    return {'status':'success'}
            
def item_del(rows):
    for row in rows:
        inst=from_dict(row)
        inst.delete()
    return {'status':'success'}

    