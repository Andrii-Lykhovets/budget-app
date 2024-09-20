from django.shortcuts import render, redirect
from django.urls import reverse

from . import cash_flow_db
from .cash_flow_db import insert_new_transaction_record
from .transactions_form import TransactionForm


def render_transaction(request):
    transaction_dict = {
        'id': 6,
        'income': 35000,
        'expense': 0,
        'description': 'Дохід від реалізації послуг',
        'company': 'Big Plus',
        'date_time': '13 July 2024 13:05',
    }
    return render(
        request,
        'example/template_transaction.html',
        context=transaction_dict,
    )


# render function looks into templates folder for a given template mane


def render_real_transactions(request):
    transactions_list = {'all_transactions': cash_flow_db.get_all_transaction_records()}
    return render(
        request,
        'example/template_real_transactions.html',
        context=transactions_list,
    )


def render_transaction_form(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            insert_new_transaction_record(form.cleaned_data)
            return redirect(reverse('example:real_transactions'))
    else:
        form_dict = {'form': TransactionForm()}
        return render(
            request,
            'example/transactions_form.html',
            context=form_dict,
        )
