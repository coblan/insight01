# encoding:utf-8

from helpers.director.engine import BaseEngine,can_list,can_touch,fa,page
from helpers.director.shortcut import page_dc
from django.contrib.auth.models import User,Group
from employee.models import EmployeeModel,BasicInfo
from workload.models import Work,WorkRecord
from .pages import WXHome


class PcEngine(BaseEngine):
    url_name='pc_engine'
    menu=[
        {'label':'home','url':'/','icon':fa('fa-home')},
        {'label':'账号管理','url':page('user'),'icon':fa('fa-key'),'visible':can_list((User,Group)),
         'submenu':[
             {'label':'用户管理','url':page('user'),'visible':can_touch(User)},
             {'label':'用户组','url':page('group'),'visible':can_touch(Group)},
             ]},
        {'label':'员工管理','icon':fa('fa-users'),'visible':can_list((BasicInfo,EmployeeModel)),
         'submenu':[
             #{'label':'部门管理','url':page('department'),'visible':can_touch(Department)},    
             {'label':'员工名册','url':page('employee'),'visible':can_touch(EmployeeModel)},
             #{'label':'工资记录','url':page('salary'),'visible':can_touch(SalaryRecords)},
             ]},
        {'label':'工作管理','icon':fa('fa-suitcase'),'visible':can_list((Work,WorkRecord)),
         'submenu':[{'label':'工时目录','url': page('workindex'),'visible':can_touch(Work)},
                    {'label':'工作类型','url': page('work'),'visible':can_touch(Work)},
                    {'label':'工作记录','url':page('workrecord'),'visible':can_touch(WorkRecord)}
                    ]
         },
        {'label':'留言','url':page('comment'),'icon':fa('fa-home')},
        #{'label':'Page Admin','url':page('webpage'),'icon':fa('fa-home'),'visible':can_touch(WebPage)},
    
    ]    

PcEngine.add_pages(page_dc)

class WxEngine(BaseEngine):
    url_name='wx_engine'
    prefer='wx'
    menu=[
        {'label':'home','url':page('home.wx'),'icon':fa('fa-home fa-2x')},
        {'label':'员工名册','url':page('employee.wx'),'visible':can_touch(EmployeeModel)},
        {'label':'工作类型(目录)','url':page('workindex.wx'),'visible':can_touch(EmployeeModel)},
        {'label':'工作类型','url':page('work.wx'),'visible':can_touch(EmployeeModel),'icon':fa('fa-suitcase fa-2x')},
        {'label':'工作记录','url':page('workrecord.wx'),'visible':can_touch(EmployeeModel),'icon':fa('fa-suitcase fa-2x')},
        {'label':'自我工作','url':page('wkself.wx'),'visible':can_touch(EmployeeModel)},
        {'label':'提意见','url':page('commentself.wx'),'visible':can_touch(EmployeeModel)},
        {'label':'管理意见','url':page('comment.wx'),'visible':can_touch(EmployeeModel)},
        
    ]

WxEngine.add_pages(page_dc)
WxEngine.add_pages({'home.wx':WXHome})