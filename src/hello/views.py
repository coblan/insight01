from django.shortcuts import render
from helpers.director import kv

def help_view(request):
    ctx={
        'help_text':kv.get_value('help_text','')
    }

    return render(request,'hello/help.html',context=ctx)