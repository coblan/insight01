# encoding:utf-8

from helpers.director.shortcut import ModelPermit
from helpers.director.db_tools import to_dict,model_to_name,from_dict
from .models import Work,Index
from django.core.exceptions import PermissionDenied

class DirMan(object):
    def __init__(self,dir_model,item_model):
        self.DIR=dir_model
        self.ITEM=item_model

    def dir_data(self,par,user):
        par_permit=ModelPermit(self.DIR,user)
        item_perm=ModelPermit(self.ITEM,user)
        if not par_permit.readable_fields():
            raise PermissionDenied,'can not read %s'% model_to_name(self.DIR)    
        if not item_perm.readable_fields():
            raise PermissionDenied,'can not read %s'%model_to_name(self.ITEM)
        
        DIR=self.DIR
        ITEM=self.ITEM    
       
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
            items=[to_dict(item,include=item_perm.readable_fields()) for item in ITEM.objects.filter(par_id=par)]
        else:
            items=[to_dict(item,include=item_perm.readable_fields()) for item in ITEM.objects.filter(par=None)]
        return {'dirs':rows,'parents':parents,'items':items}
    
    
    def dir_create(self,user,par=None):
        if not ModelPermit(self.DIR,user).can_add():
            raise PermissionDenied,'not permit create %s'%model_to_name(self.DIR)
        
        if not par:
            i = self.DIR.objects.create()
        else:
            i = self.DIR.objects.create( par_id=par)
        return to_dict(i)
    
    def item_create(self,par,user):
        if not ModelPermit(self.ITEM,user).can_add():
            raise PermissionDenied,'can not create %s'%model_to_name( self.ITEM)
        
        par= par or None
        work = self.ITEM.objects.create(par_id=par)
        return to_dict(work)
    
    
    def items_paste(self,rows,par,user):
        """粘贴 dir 和 item """
        if par:
            par_inst=self.DIR.objects.get(pk=par)
        else:
            par_inst=None
        for row in rows:
            inst = from_dict(row)
            if 'par' in  ModelPermit(inst,user).changeable_fields():
                inst.par=par_inst
                inst.save()
            else:
                raise PermissionDenied,'can not modify par of %s'% model_to_name(inst)
        return {'status':'success'}
     
    def item_del(self,rows,user):
        """ 删除 dir 和 item """
        for row in rows:
            inst=from_dict(row)
            if ModelPermit(inst,user).can_del():
                inst.delete()
            else:
                raise PermissionDenied,'can not delete %s'% model_to_name(inst)
        return {'status':'success'}    