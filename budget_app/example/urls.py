from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lesson/', views.simple_lesson_view, name='lesson'),
    path('homework/', views.homework_view, name='homework'),
    path('template_example/', views.render_template_example, name='template_example'),
    path('template_vars/', views.render_templated_with_variables, name='template_vars'),
]
