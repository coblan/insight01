from django.shortcuts import render
from django.contrib.auth.models import User
from helpers.director.db_tools import model_to_head,to_dict
from .models import EmployeeModel,BasicInfo
from .admin import BasicInfoFields
# Create your views here.

def my_info(request):
    user= request.user
    ctx={'username':user.username}
    emp= EmployeeModel.objects.filter(user=request.user).first()
    if not emp:
        ctx['no_emp']=True
    else:
        bf=BasicInfoFields(crt_user=user)
        ctx['base_heads']=bf.get_heads()
        ctx['base_row']=bf.get_row()
    return render(request,'employee/my_info.html',context=ctx)