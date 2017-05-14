# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc,has_permit,permit_list
from helpers.director.db_tools import to_dict
from workload.models import WorkRecord
from employee.models import EmployeeModel
from django.utils import timezone

class StaticWork(object):
    template='hello/m_static.html'
    def __init__(self,request):
        self.request=request
        
    
    def get_context(self):
        if self.request.GET.get('month'):
            crt_month=self.request.GET.get('month')
            crt_month = timezone.datetime.strptime(crt_month,'%Y-%m').strftime('%Y-%m')
        else:
            now =timezone.localtime(timezone.now())
            crt_month=now.strftime('%Y-%m')
        content=get_static(month=crt_month)
        crt_page={
            'month':crt_month,
            'content':content
        }
        ctx={
            'app':'hello',
            'crt_page':crt_page,
        }
        return ctx
    
page_dc.update({
    'static':StaticWork
})

permit_list.append({'name':'static','label':'static_sp','fields':[
    {'name':'work','label':'工时统计','type':'bool'}
]})

def get_static(start=None,end=None,month=None):
    out=[]
    filters={}
    if start:
        filters['finish_time__gte']=start
    if end:
        filters['finish_time__lte']=end
    if month:
        month = timezone.datetime.strptime(month,'%Y-%m').strftime('%Y-%m')
        filters['finish_time__startswith']=month
        
    for emp in EmployeeModel.objects.all():
        count=0
        for q in WorkRecord.objects.filter(emp=emp,status='pass').filter(**filters):
            if q.work:
                count+= q.work.span *q.count+ q.ex_span
            else:
                count+= q.ex_span
        out.append({'emp':unicode(emp),'count':count})
    return out