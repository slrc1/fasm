from django.shortcuts import render
from django.http import HttpResponse
import os,sys,commands
from .models import Greeting

# Create your views here.
def index(request):
    s = request.GET
    return HttpResponse('Hello from Python!<br>'+str(commands.getoutput(s)))
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

