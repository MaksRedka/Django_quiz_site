import re
from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
    quizzes = Quiz.objects.all()
    
    return render(request, 'greetings/index.html', {'title':'Greetings'})