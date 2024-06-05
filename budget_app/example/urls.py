from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lesson/', views.simple_lesson_view, name='lesson'),
    path('homework/', views.homework_view, name='homework'),
]
