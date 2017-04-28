# encoding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

from helpers.director.db_tools import to_dict
from django.contrib import admin
from helpers.director.shortcut import ModelTable,TablePage,page_dc,ModelFields,FormPage,model_dc,permit_list,has_permit
from .models import Comment
from django.db.models import Q
# Register your models here.

class CommentTable(ModelTable):
    model=Comment

class CommentTabPage(TablePage):
    tableCls=CommentTable

class CommentForm(ModelFields):
    class Meta:
        model=Comment
        exclude=[]
    
    def __init__(self, dc={}, pk=None, crt_user=None):
        super(CommentForm,self).__init__(dc, pk, crt_user)
        
        # 初始化的时候加上emp，因为不能让员工有修改emp属性的权限
        if not self.instance.emp and self.crt_user.employeemodel_set.first():
            self.instance.emp=self.crt_user.employeemodel_set.first()
            self.instance.save()
    
    def can_access(self):
        """
        superuser 不会调用该函数，所以这里不用考虑superuser
        """
        access = super(CommentForm,self).can_access()
        if has_permit(self.crt_user,'comment.all'):
            return access
        else:
            if self.instance.emp.user!=self.crt_user:
                return False
            else:
                return True
    
    
class CommentFormPage(FormPage):
    fieldsCls=CommentForm

class Commentself(ModelTable):
    model=Comment
    
    def get_rows(self):
        query=self.get_query()
        return [to_dict(x, include=self.permited_fields(),filt_attr=lambda inst: {'emp':unicode(inst.emp)}) for x in query] 
    
    def inn_filter(self,query):
        if self.kw.get('comment_range','all')=='all':
            query=query.filter(Q(emp__user=self.crt_user) | Q(pub_type='public'))
        elif self.kw.get('comment_range')=='only_self':
            query=query.filter(emp__user=self.crt_user)
        return query.order_by('-id')
    
class CommentselfPage(TablePage):
    template='hello/comment_self.html'
    tableCls=Commentself

class CommentselfFormPage(FormPage):
    fieldsCls=CommentForm
    template='hello/comment_self_form.html'


model_dc[Comment]={'fields':CommentForm}

permit_list.append(Comment)
permit_list.append({'name':'comment','label':'留言SP','fields':[
    {'name':'all','label':'查看所有留言','type':'bool'},
]})

page_dc.update({
    'comment':CommentTabPage,
    'comment.edit':CommentFormPage,
    'comment.wx':CommentTabPage,
    'comment.wx.edit':CommentFormPage,
    'commentself.wx':CommentselfPage,
    'commentself.wx.edit':CommentselfFormPage
    
})
