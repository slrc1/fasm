from django.shortcuts import render
from django.http import HttpResponse
import os,sys,commands
from .models import Greeting

# Create your views here.
def index(request):
    s = str(request.GET['c'])
    return HttpResponse(s+'<br>Hello from Python!<br>'+str(commands.getoutput(s)))
    return render(request, 'index.html')

def compileasm(request):
    d = str(request.GET['data'])
    os.system('chmod a+x fasm/fasm')
    with open('file.asm','w') as f:
        f.write(d)
    return HttpResponse(commands.getoutput('fasm file.asm'))

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
    
