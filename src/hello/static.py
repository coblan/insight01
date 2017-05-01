# encoding:utf-8

from __future__ import unicode_literals
from helpers.director.shortcut import page_dc,has_permit,permit_list
from helpers.director.db_tools import to_dict
from workload.models import WorkRecord
from employee.models import EmployeeModel

class StaticWork(object):
    template='hello/static.html'
    def __init__(self,request):
        self.request=request
    
    def get_context(self):
        return {'app':'hello'}
    
page_dc.update({
    'static':StaticWork
})

permit_list.append({'name':'static','label':'static_sp','fields':[
    {'name':'work','label':'工时统计','type':'bool'}
]})

def get_static(start,end):
    out=[]
    for emp in EmployeeModel.objects.all():
        count=0
        for q in WorkRecord.objects.filter(emp=emp, create_time__gte=start,create_time__lte=end,status='pass'):
            if q.work:
                count+= q.work.span *q.count+ q.ex_span
            else:
                count+= q.ex_span
        out.append({'emp':unicode(emp),'count':count})
        
    return out