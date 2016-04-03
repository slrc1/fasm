from django.shortcuts import render
from django.http import HttpResponse
import os,sys,subprocess
from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!<br>'+str(subprocess.getoutput('fasm')))
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

