from django.shortcuts import render
from django.http import HttpResponse
import os,sys,commands
from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!<br>'+str(commands.getoutput('tar fasm-1.71.51.tar')))
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

