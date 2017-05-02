# encoding:utf-8

from helpers.director.db_tools import to_dict
from .models import Work,Index

class DirMan(object):
    DIR=Index
    ITEM=Work

    @classmethod
    def dir_data(cls,par):
        DIR=cls.DIR
        ITEM=cls.ITEM      
        if par:
            query = DIR.objects.filter(par_id=par)
        else:
            query = DIR.objects.filter(par=None)
        rows=[to_dict(idx) for idx in query]
        
        parents=[]
        if par:
            this_dir=DIR.objects.get(id=par)
            parents.append(this_dir)
            while this_dir.par:
                parents.append(this_dir.par)
                this_dir=this_dir.par
        parents.reverse()
        parents= [to_dict(idx) for idx in parents]
        
        items=[]
        if par:
            # this_dir=DIR.objects.get(id=par)
            items=[to_dict(item) for item in ITEM.objects.filter(index_id=par)]
        else:
            items=[to_dict(item) for item in ITEM.objects.filter(index=None)]
        return {'dirs':rows,'parents':parents,'items':items}
    
    @staticmethod
    def dir_create(user,par=None):
        if not ModelPermit(Index,user).can_add():
            raise PermissionDenied,'not permit create index'
        if not par:
            i = Index.objects.create()
        else:
            i = Index.objects.create( par_id=par)
        return to_dict(i)
    
    @staticmethod
    def item_create(par):
        par=par or None
        work = Work.objects.create(index_id=par)
        return to_dict(work)
    
    @staticmethod
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
    @staticmethod      
    def item_del(rows):
        for row in rows:
            inst=from_dict(row)
            inst.delete()
        return {'status':'success'}    