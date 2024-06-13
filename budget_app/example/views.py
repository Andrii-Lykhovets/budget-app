from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse('<h1>this is an index page</h1>')


def simple_lesson_view(request):
    return HttpResponse('this view was created during the lesson')


def homework_view(request):
    return HttpResponse('This is my homework!')


def render_template_example(request):
    return render(request, 'example/template_example.html')


def render_templated_with_variables(request):
    rendered_variables = {
        'example_var': 'This is how the story went: I met someone by accident.',
        'a_list': [1, 2, 3],
        'a_dict': {
            'random': 42,
            'key1': 'that opens the door 1',
        }
    }
    return render(
        request,
        'example/template_with_variables.html',
        context=rendered_variables,
    )
