from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('<h1>this is an index page</h1>')


def simple_lesson_view(request):
    return HttpResponse('this view was created during the lesson')


def homework_view(request):
    return HttpResponse('This is my homework!')
