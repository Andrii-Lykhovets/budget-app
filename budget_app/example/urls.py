from django.urls import path
from . import views, transaction_view

# this file is responsible for managing (giving path to) views

urlpatterns = [
    path('', views.index, name='index'),
    path('lesson/', views.simple_lesson_view, name='lesson'),
    path('homework/', views.homework_view, name='homework'),
    path('template_example/', views.render_template_example, name='template_example'),
    path('template_vars/', views.render_templated_with_variables, name='template_vars'),
    path('transaction_data/', transaction_view.render_transaction, name='transaction_data'),
    path('transactions/', transaction_view.render_real_transactions, name='real_transactions'),
]
