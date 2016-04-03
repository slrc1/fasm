from django.shortcuts import render
from django.http import HttpResponse
import os,sys
from .models import Greeting

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!\n'+sys.platform+'\n'+os.name+'\n'+os.system('ls -l'))
    return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

