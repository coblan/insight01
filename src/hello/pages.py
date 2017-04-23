


class WXHome(object):
    template='wx/home.html'
    need_login=False
    def __init__(self,request):
        self.request=request
    
    def get_context(self):
        return {}

