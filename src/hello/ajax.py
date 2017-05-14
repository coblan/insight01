import static
def get_global():
    return globals()

def get_static(month):
    return {'status':'success','items':static.get_static(month=month)}