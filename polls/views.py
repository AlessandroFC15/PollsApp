from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    context = {'questions_list': Question.objects.all()}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = None

    try:
        question = Question.objects.get(pk=question_id)
    except:
        print("Question with id " + question_id + " was not found")

    context = {'question': question}

    return render(request, 'polls/detail.html', context)