# encoding:utf-8

from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import models
from employee.models import EmployeeModel
# Create your models here.

class Index(models.Model):
    name=models.CharField('name',max_length=500,blank=True)
    par = models.ForeignKey('self',verbose_name='parent dir',blank=True,null=True,related_name='childs')
    

WORK_STATUS=(
    ('pass','通过'),
    ('unpass','未通过'),
    ('waiting','等待审核')
)

class Work(models.Model):
    index =models.ForeignKey(Index,verbose_name='目录',blank=True,null=True)
    name= models.CharField('名称',max_length=100,default='')
    span = models.FloatField('工时',default=0,help_text='单位(小时)')
    status=models.CharField('状态',max_length=20,choices=WORK_STATUS,default='waiting')
    tag = models.CharField('标签',max_length=500,blank=True)
    detail=models.TextField(verbose_name='详细',blank=True)

class WorkRecord(models.Model):
    work=models.ForeignKey(Work,verbose_name='工作',blank=True,null=True)
    emp=models.ForeignKey(EmployeeModel,verbose_name='员工',blank=False)
    ex_span=models.FloatField('调整工时',default=0,help_text='单位(小时)')
    status=models.CharField('状态',max_length=20,choices=WORK_STATUS,default='waiting')
    detail=models.TextField(verbose_name='详细',blank=True)
    create_time=models.DateTimeField(verbose_name='创建时间',auto_now=True)
    