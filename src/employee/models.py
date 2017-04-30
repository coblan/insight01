from __future__ import unicode_literals

from django.contrib.auth.models import User,Group
from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.

class EmployeeModel(models.Model):
    user = models.ForeignKey(User,verbose_name=_('account'), blank=True, null=True)
    baseinfo=models.OneToOneField('BasicInfo',verbose_name=_('basic info'),blank=True,null=True)
   
    def __init__(self,*args,**kw):
        super(EmployeeModel,self).__init__(*args,**kw)
        if not self.baseinfo:
            self.baseinfo=BasicInfo()
       
    def __unicode__(self):
        if self.baseinfo:
            return self.baseinfo.name
        else:
            return 'unnamed employee'
GEN=(
    ('male',_('male')),
      ('femal',_('femal'))
      )
     
class BasicInfo(models.Model):
    name = models.CharField(_('name'), max_length=50, blank=True)
    age = models.CharField(_('age'), max_length=50, blank=True)
    head = models.CharField(_('head image'),max_length=200,blank=True)
    id_number=models.CharField(_('id  number'),max_length=200,blank=True)
    address=models.CharField(_('address'),max_length=500,blank=True)
    gen = models.CharField(_('gen'),max_length=30,blank=True,choices=GEN)
    phone = models.CharField(_('phone'),max_length=100,blank=True)
    
    def __init__(self,*args,**kw):
        super(BasicInfo,self).__init__(*args,**kw)
        if not self.head:
            self.head='/static/image/user.jpg'
            
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name=_('basic info')
