# encoding:utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from employee.models import EmployeeModel
from helpers.director.model_validator import has_str
from django.utils import timezone
# Create your models here.

class Index(models.Model):
    name=models.CharField('name',max_length=500,default='new index',validators=[has_str])
    par = models.ForeignKey('self',verbose_name='parent dir',blank=True,null=True,related_name='childs')
    
    def __unicode__(self):
        return self.name
    

WORK_STATUS=(
    ('pass','通过'),
    ('unpass','未通过'),
    ('waiting','等待审核')
)

class Work(models.Model):
    index =models.ForeignKey(Index,verbose_name='目录',blank=True,null=True)
    name= models.CharField('名称',max_length=100,default='new work',validators=[has_str])
    span = models.FloatField('工时',default=0,help_text='单位(小时)')
    status=models.CharField('状态',max_length=20,choices=WORK_STATUS,default='waiting')
    tag = models.CharField('标签',max_length=500,blank=True)
    detail=models.TextField(verbose_name='详细',blank=True)
    desp_img=models.CharField('描述图片',max_length=300,blank=True)
    
    def __unicode__(self):
        return self.name

class WorkRecord(models.Model):
    work=models.ForeignKey(Work,verbose_name='工作',null=True)
    emp=models.ForeignKey(EmployeeModel,verbose_name='员工',blank=False,null=True)
    ex_span=models.FloatField('调整工时',default=0,help_text='单位(小时)')
    status=models.CharField('状态',max_length=20,choices=WORK_STATUS,default='waiting')
    short=models.CharField('简短描述',max_length=300,blank=True)
    detail=models.TextField(verbose_name='详细',blank=True)
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now=True)
    desp_img=models.CharField('描述图片',max_length=300,blank=True)
    #tmp=models.BooleanField('临时工时',default=False)
    
    def __unicode__(self):
        if self.work:
            return '%(work)s_%(emp)s | %(create_time)s'%{'work':self.work,'emp':self.emp,'create_time':timezone.localtime( self.create_time).strftime('%Y-%m-%d %H:%M:%S')}
        else:
            return 'unnamed workrecord'
    