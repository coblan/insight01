# encoding:utf-8

from helpers.director.db_tools import from_dict

def save_self_info(base_info,user):
    """
    """
    instance = from_dict(base_info)
    if not instance.employeemodel:
        emp =user.employeemodel_set.first()
        emp.baseinfo=instance
        emp.save()
    elif instance.employeemodel and instance.employeemodel.user==user:
        instance.save()
    else:
        return {'status':'error','msg':'base info not match with current user'}
    return {"status":'success'}
    