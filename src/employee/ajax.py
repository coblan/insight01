# encoding:utf-8

from helpers.director.db_tools import from_dict


def get_global():
    return globals()

def save_self_info(base_info,user):
    """
    """
    instance = from_dict(base_info)
    if getattr(instance,'employeemodel',None) is None:
        emp =user.employeemodel_set.first()
        emp.baseinfo=instance
        emp.save()
    elif instance.employeemodel and instance.employeemodel.user==user:
        instance.save()
    else:
        return {'status':'error','msg':'base info not match with current user'}
    return {"status":'success'}
    