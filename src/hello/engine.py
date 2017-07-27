# encoding:utf-8

from helpers.director.engine import BaseEngine,can_list,can_touch,fa,page,and_list
from helpers.director.shortcut import page_dc,has_permit
from django.contrib.auth.models import User,Group
# from employee.models import EmployeeModel,BasicInfo
# from workload.models import Work,WorkRecord
from helpers.pageadaptor.models import WebPage
from hello.models import Comment
from .pages import WXHome
from helpers.director.models import KVModel
from django.core.urlresolvers import reverse
from helpers.maintenance.update_static_timestamp import static_file_timestamp_dict
from helpers.case.organize import menu as organize_menu
from helpers.case.work import menu as work_menu
from helpers.pageadaptor.shotcut import Press
from helpers.case.map_daka import menu as map_daka_menu
from django.views.decorators.cache import cache_control

class PcEngine(BaseEngine):
    url_name='pc_engine'
    menu=[
        {'label':'home','url':'/','icon':fa('fa-home')},
        {'label':'账号管理','url':page('user'),'icon':fa('fa-key'),'visible':can_list((User,Group)),
         'submenu':[
             {'label':'用户管理','url':page('user'),'visible':can_touch(User)},
             {'label':'用户组','url':page('group'),'visible':can_touch(Group)},
             ]},
        
        organize_menu.pc_menu,
        work_menu.pc_menu,
        
        # {'label':'员工管理','icon':fa('fa-users'),'visible':can_list((BasicInfo,EmployeeModel)),
         # 'submenu':[
             # #{'label':'部门管理','url':page('department'),'visible':can_touch(Department)},    
             # {'label':'员工名册','url':page('employee'),'visible':can_touch(EmployeeModel)},
             # #{'label':'工资记录','url':page('salary'),'visible':can_touch(SalaryRecords)},
             # ]},
        # {'label':'工作管理','icon':fa('fa-suitcase'),'visible':can_list((Work,WorkRecord)),
         # 'submenu':[{'label':'工时目录','url': page('workindex'),'visible':can_touch(Work)},
                    # {'label':'工时类型','url': page('work'),'visible':can_touch(Work)},
                    # {'label':'工作记录','url':page('workrecord'),'visible':can_touch(WorkRecord)}
                    # ]
         # },
         
        {'label':'留言','url':page('comment'),'icon':fa('fa-home')},
        {'label':'设置','url':page('kv'),'icon':fa('fa-home'),'visible':can_touch(KVModel)},
        {'label':'Page Admin','url':page('webpage'),'icon':fa('fa-home'),'visible':can_touch(WebPage)},
    
    ]    

PcEngine.add_pages(page_dc)

class WxEngine(BaseEngine):
    url_name='wx_engine'
    prefer='wx'
    root_page='/wx/home.wx'
    
    def __init__(self):
        self.root_page= page('home.wx')
            
    menu=organize_menu.wx_menu+ \
        work_menu.wx_menu +[
        # {'label':'home','url':page('home.wx'),'icon':fa('fa-home fa-2x')},
        # {'label':'员工名册','url':page('employee.wx'),'visible':can_touch(EmployeeModel),'icon':fa('fa-users fa-2x')},
        # {'label':'工时类型(目录)','url':page('workindex.wx'),'visible':can_touch(Work),'icon':fa('fa-clock-o fa-2x')},
        #{'label':'工时类型','url':page('work.wx'),'visible':can_touch(EmployeeModel),'icon':fa('fa-suitcase fa-2x')},
        # {'label':'工作提交','url':page('wkself.wx'),'icon':fa('fa-hand-paper-o fa-2x'),\
         # 'visible':and_list([WorkRecord,lambda user: not user.is_anonymous() and user.employeemodel_set.exists()]),},
        # {'label':'工作审核','url':page('workrecord.wx','?status=waiting'),'visible':and_list(['workrecord.check_all',WorkRecord]),'icon':fa('fa-eye fa-2x')},
        
        {'label':'意见','url':page('commentself.wx'),'visible':can_touch(Comment),'icon':fa('fa-pencil-square-o fa-2x')},
        #{'label':'管理意见','url':page('comment.wx'),'visible':and_list([Comment,'comment.all']),'icon':fa('fa-pencil-square fa-2x')},
        
        {'label':'统计','url':page('static'),'icon':fa('fa-bar-chart fa-2x'),'visible':and_list( ['static.work'])},
        
    ]
    
    def custome_ctx(self, ctx):
        help_name = 'help_'+ctx['page_name']
        ctx['stamp']=static_file_timestamp_dict
        engine_press=Press(help_name)
        if engine_press.page:
            ctx['help_url']=self.get_url('press')+'?_name=%s'%help_name
        return ctx    

WxEngine.add_pages(page_dc)
WxEngine.add_pages({'home.wx':WXHome})



class F7Engine(BaseEngine):
    url_name='f7_engine'
    prefer='f7'
    root_page='/f7/home.f7'
    
    menu=organize_menu.f7_menu+ \
        work_menu.f7_menu  + \
        map_daka_menu.f7_menu
    
    def custome_ctx(self, ctx):
        ctx['stamp']=static_file_timestamp_dict
        
        help_name = 'help_'+ctx['page_name']
        engine_press=Press(help_name)
        if engine_press.page:
            ctx['help_url']=self.get_url('press')+'?_name=%s'%help_name
        return ctx  
    
    # @cache_control(max_age=0,must_revalidate=True)
    # def view(self, request, name):
        # return super(F7Engine,self).view(request,name)

class F7FrameWraper(object):
    template='f7/frame_wraper.html'
    def __init__(self,request):
        src= request.GET.get('src')
        self.src=urllib.unquote( src)
        
    def get_context(self):
        return {'src':self.src}
    
F7Engine.add_pages(page_dc)
F7Engine.add_pages({'f7.html':F7FrameWraper})