import static
def get_global():
    return globals()

def get_static(start,end):
    return {'status':'success','items':static.get_static(start, end)}