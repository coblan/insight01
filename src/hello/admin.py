# encoding:utf-8
from __future__ import unicode_literals
from __future__ import absolute_import

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
        
        # 初始化的时候加上employee，因为不能让员工有修改emp属性的权限
        if not self.instance.emp and self.crt_user.employeemodel_set.first():
            self.instance.emp=self.crt_user.employeemodel_set.first()
    
    def can_access(self):
        access = super(CommentForm,self).can_access()
        if has_permit(self.crt_user,'all_comment'):
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
    def inn_filter(self,query):
        query=query.filter(Q(emp__user=self.crt_user) | Q(pub_type='public'))
        return query
    
class CommentselfPage(TablePage):
    template='hello/comment_self.html'
    tableCls=Commentself

model_dc[Comment]={'fields':CommentForm}

permit_list.append(Comment)
permit_list.append({'name':'comment_sp','label':'留言','fields':[
    {'name':'all_comment','label':'查看所有留言','type':'bool'},
]})

page_dc.update({
    'comment':CommentTabPage,
    'comment.edit':CommentFormPage,
    'comment.wx':CommentTabPage,
    'comment.wx.edit':CommentFormPage,
    'commentself.wx':CommentselfPage,
    
})
