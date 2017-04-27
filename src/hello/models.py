from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _
from employee.models import EmployeeModel

# Create your models here.
PUB_TYPE=(
    ('public',_('Public')),
    ('private',_('Private'))
)

class Comment(models.Model):
    emp=models.ForeignKey(EmployeeModel,verbose_name=_('employee'),blank=True,null=True)
    content=models.TextField(verbose_name=_('content'),blank=True,null=True)
    create_time=models.DateTimeField(verbose_name=_('create time'),auto_now=True)
    rep_content=models.TextField(verbose_name=_('reply content'),blank=True,null=True)
    pub_type=models.CharField(_('publish type'),max_length=50,choices=PUB_TYPE,default='public')
    