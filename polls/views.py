from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    context = {'questions_list': Question.objects.all()}
    return render(request, 'polls/index.html', context)


def test_view(request):
    return HttpResponse('This is the test view!')